my_list = input('write some words: ').split()

for i, el in enumerate(my_list, 1):
    print(i, el[0:10])