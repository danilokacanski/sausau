#%% md
# # Zadaci za vezbu
#%% md
# ## Zadatak 1 - Presek dva niza (LeetCode ID: 349)
#%%
def presek_nizova(nums1, nums2):
    return list(set(nums1) & set(nums2))
#%%
print(presek_nizova([4, 9, 5], [9, 4, 9, 8, 4]))
#%% md
# ## Zadatak 2 - Pronadji poziciju (LeetCode ID: 35)
#%%
def pronadji_poziciju(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low
#%%
print(pronadji_poziciju([1, 3, 5, 6], 5))
#%% md
# ## Zadatak 3 - Koren (LeetCode ID: 69)
#%%
def koren(x):
    if x < 2:
        return x

    low, high = 1, x
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            low = mid + 1
        else:
            high = mid - 1
    return high
#%%
print(koren(17))
#%% md
# ## Zadatak 4 - Nedostajuc broj (LeetCode ID: 268)
#%%
def missingNumber1(nums):
        n = len(nums)
        num_set = set(nums)

        for i in range(n + 1):
            if i not in num_set:
                return i
#%%
def missingNumber2(nums):
    n = len(nums)
    ocekivana_suma = n * (n + 1) // 2
    stvarna_suma = sum(nums)
    return ocekivana_suma - stvarna_suma
#%%
print(missingNumber2([3, 0, 1]))
print(missingNumber2([0, 1]))
print(missingNumber2([9,6,4,2,3,5,7,0,1]))
#%% md
# ## Zadatak 5 - Vise ili manje (LeetCode ID: 374)
#%%
tajni_broj = 42  # Promeni po želji

def guess(num):
    if num == tajni_broj:
        return 0
    elif num > tajni_broj:
        return -1
    else:
        return 1
#%%
def guessNumber(n):
    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2
        rezultat = guess(mid)

        if rezultat == 0:
            return mid
        elif rezultat == -1:
            high = mid - 1
        else:
            low = mid + 1
#%%
print(guessNumber(100))