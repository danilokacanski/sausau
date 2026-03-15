#%% md
# # Zadaci za vezbu
#%% md
# ## Zadatak 1 - Suma dva broja
#%%
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
#%%
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
#%% md
# ## Zadatak 2 - Uklanjanje duplikata
#%%
def remove_duplicates(nums):
    if not nums:
        return 0

    unique = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            unique.append(nums[i])

    for i in range(len(unique)):
        nums[i] = unique[i]

    return len(unique)
#%%
nums = [8,5,4,3,3,2,1]
print(remove_duplicates(nums))
#%% md
# ## Zadatak 3 - Plus 1
#%%
def plus_one(digits):
    broj = 0
    for cifra in digits:
        broj = broj * 10 + cifra

    broj += 1
    rezultat = [int(c) for c in str(broj)]
    return rezultat
#%%
digits = [4,3,2,9]
print(plus_one(digits))
#%% md
# ## Zadatak 4 - Spajanje sortiranih nizova
#%%
def merge(nums1, m, nums2, n):
    # Uzmi samo korisne delove nums1 i nums2
    deo1 = nums1[:m]
    deo2 = nums2

    # Spoji obe liste i sortiraj
    spojeno = deo1 + deo2
    spojeno.sort()

    # Upisi rezultat nazad u nums1
    for i in range(len(spojeno)):
        nums1[i] = spojeno[i]
    print(nums1)
#%%
merge([1,2,3,0,0,0],3,[2,5,6],3)
#%% md
# ## Zadatak 5 - Vecinski eleemnt
#%%
def majorityElement(nums):
    counts = {}

    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    n = len(nums)
    for key in counts:
        if counts[key] > n // 2:
            return key
#%%
nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
#%% md
# ## Zadatak 6 - Nedostajuci broj
#%%
def missingNumber(nums):
    n = len(nums)
    num_set = set(nums)

    for i in range(n + 1):
        if i not in num_set:
            return i
#%%
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missingNumber(nums))
#%% md
# ## Teemov napad
#%%
def findPoisonedDuration(timeSeries, duration):
    if not timeSeries:
        return 0

    total = 0
    for i in range(len(timeSeries) - 1):
        gap = timeSeries[i + 1] - timeSeries[i]
        total += min(gap, duration)

    return total + duration
#%%
timeSeries = [1, 4]
duration = 2
print(findPoisonedDuration(timeSeries, duration))