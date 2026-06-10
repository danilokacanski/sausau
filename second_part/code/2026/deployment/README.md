# Car Evaluation Deployment Example

# Project structure

* `src/main.py` - loads the dataset, preprocesses the data, trains and evaluates several ML models and saves the final model pipeline.
* `src/predict.py` - loads the saved model and performs prediction for one new example.
* `app/api.py` - provides a simple FastAPI endpoint for using the saved model through an API.
* `app/ui.py` - provides a simple Streamlit interface for entering car features and displaying the model prediction.
