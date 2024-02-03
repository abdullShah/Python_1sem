arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
arr_all = []

k_1 = 0
k_2 = 0

for q in range(len(arr_2) + len(arr_1)):
    if k_1 == len(arr_1):
        arr_all.append(arr_2[k_2])
        k_2 += 1
        continue

    if k_2 == len(arr_2):
        arr_all.append(arr_1[k_1])
        k_1 += 1
        continue

    if arr_1[k_1] <= arr_2[k_2]:
        arr_all.append(arr_1[k_1])
        k_1 += 1
    else:
        arr_all.append(arr_2[k_2])
        k_2 += 1

print(arr_all)

ind_min = 0
val_min = float("inf")
ind_max = 0
val_max = float("-inf")

for i in range(len(arr_all)):
    if val_min > arr_all[i] and abs(arr_all[i]) % 2 == 0:
        val_min = arr_all[i]
        ind_min = i
    if val_max < arr_all[i] and abs(arr_all[i]) % 2 == 1:
        val_max = arr_all[i]
        ind_max = i

arr_all[ind_min], arr_all[ind_max] = arr_all[ind_max], arr_all[ind_min]

print(arr_all)
