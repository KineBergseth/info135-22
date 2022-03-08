def dup_sort(string1):
    def sort_list(liste):
        for i in range(0, len(liste) - 1):
            for j in range(len(liste) - 1):
                if liste[j] > liste[j + 1]:
                    new = liste[j]
                    liste[j] = liste[j + 1]
                    liste[j + 1] = new
        return liste

    sort_list(string1)
    return list(dict.fromkeys(string1))


my_list = [5, 3, 1, 7, 4, 3, 2, 1, 2, 3, 4, 5]
print(dup_sort(my_list))

