print("\n Oppgave 3")


def finn_minste(arr):
    minste = arr[0]
    minste_indeks = 0
    for i in range(1, len(arr)):
        if arr[i] < minste:
            minste = arr[i]
            minste_indeks = i
        return minste_indeks


def sort_and_rem_dup(arr):
    new_list = []
    for pass_num in range(len(arr) - 1, 0, -1):

        for i in range(pass_num):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    for value in arr:
        if value not in new_list:
            new_list.append(value)
    return new_list


my_list = [5, 4, 3, 2, 1, 2, 3, 4, 5]
new_list = sort_and_rem_dup(my_list)
print(new_list)
