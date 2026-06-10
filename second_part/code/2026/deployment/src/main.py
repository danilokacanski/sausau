from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data" / "car_evaluation.csv"
MODEL_DIR = BASE_DIR / "models"
RESULTS_DIR = BASE_DIR / "results"
FIGURES_DIR = RESULTS_DIR / "figures"

MODEL_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)
FIGURES_DIR.mkdir(parents=True, exist_ok=True)


# Učitavanje podataka
dataset = pd.read_csv(DATA_PATH, encoding="utf-8")

print("Prvih nekoliko redova")
print(dataset.head())

print("\nDimenzije skupa")
print(dataset.shape)


# Feature selection - irelevantni atributi
# carID predstavlja identifikator reda i ne nosi korisnu informaciju za predikciju klase
dataset = dataset.drop(columns=["carID"])


# Provera nedostajućih vrednosti
print("\nNedostajuće vrednosti pre čišćenja")
print(dataset.isna().sum())

dataset = dataset.dropna()

print("\nNedostajuće vrednosti nakon čišćenja")
print(dataset.isna().sum())


# Provera duplikata
print("\nBroj duplikata")
print(dataset.duplicated().sum())

dataset = dataset.drop_duplicates()


# Ulazni atributi i ciljna promenljiva
X = dataset[["buying", "maintenance", "doors", "persons", "lug_boots", "safety"]]
y = dataset["class"]

print("\nRaspodela ciljnih klasa")
print(y.value_counts())


# EDA - raspodela ciljnih klasa
class_counts = y.value_counts()

plt.figure(figsize=(8, 5))
class_counts.plot(kind="bar")
plt.title("Class distribution")
plt.xlabel("Class")
plt.ylabel("Number of samples")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "class_distribution.png")
plt.show()


# EDA - odnos atributa i ciljne promenljive
# Pošto su svi ulazni atributi kategorijski, crosstab daje pregled odnosa vrednosti atributa i klasa
print("\nOdnos atributa i ciljne promenljive")

for column in X.columns:
    print("\nAtribut:", column)
    print(pd.crosstab(dataset[column], y, normalize="index").round(2))


# Podela na trening i test skup
# stratify čuva sličnu raspodelu klasa u trening i test skupu
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nDimenzije trening skupa")
print(X_train.shape)

print("\nDimenzije test skupa")
print(X_test.shape)


# Preprocessing - enkodiranje kategorijskih atributa
# Svi ulazni atributi se tretiraju kao kategorijski
# doors i persons imaju vrednosti poput 5more i more, pa nisu čisto numerički atributi
categorical_features = ["buying", "maintenance", "doors", "persons", "lug_boots", "safety"]

preprocessor = ColumnTransformer(
    transformers=[
        ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)


# Demonstracija preprocessing koraka
# OneHotEncoder tekstualne kategorije pretvara u numerički oblik
X_train_preprocessed = preprocessor.fit_transform(X_train)

print("\nOblik X_train pre preprocessing-a")
print(X_train.shape)

print("\nOblik X_train nakon preprocessing-a")
print(X_train_preprocessed.shape)

print("\nNovi atributi nakon enkodiranja")
print(preprocessor.get_feature_names_out())


# Modeli za poređenje
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "KNN": KNeighborsClassifier(n_neighbors=7),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "SVM": SVC()
}

trained_models = {}
results = []

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)


# Treniranje i evaluacija modela
for model_name, classifier in models.items():
    print("\n" + "=" * 50)
    print(model_name)
    print("=" * 50)

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", classifier)
        ]
    )

    # Cross-validation na trening skupu
    # Pipeline omogućava da se preprocessing pravilno primeni unutar svakog fold-a
    cv_scores = cross_val_score(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring="f1_macro"
    )

    model.fit(X_train, y_train)
    trained_models[model_name] = model

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    f1_macro = f1_score(y_test, y_pred, average="macro")

    print("CV Macro F1:", cv_scores.mean())
    print("Test Accuracy:", accuracy)
    print("Test Macro F1:", f1_macro)

    print("\nClassification report")
    print(classification_report(y_test, y_pred, zero_division=0))

    print("\nConfusion matrix")
    print(confusion_matrix(y_test, y_pred))

    results.append({
        "model": model_name,
        "cv_f1_macro": cv_scores.mean(),
        "test_accuracy": accuracy,
        "test_f1_macro": f1_macro
    })


# Poređenje modela
results_data = pd.DataFrame(results)

print("\nPoređenje modela")
print(results_data.sort_values(by="test_f1_macro", ascending=False))

results_data.to_csv(RESULTS_DIR / "model_comparison.csv", index=False)


# Izbor finalnog modela
# Finalni model se bira na osnovu rezultata evaluacije i diskusije
final_model_name = "Decision Tree"
final_model = trained_models[final_model_name]


# Čuvanje modela
# Čuva se ceo pipeline, odnosno preprocessing i klasifikacioni model
MODEL_PATH = MODEL_DIR / "sausaufinal.joblib"
joblib.dump(final_model, MODEL_PATH)

print("\nFinalni model:", final_model_name)
print("Model je sačuvan u:", MODEL_PATH)
