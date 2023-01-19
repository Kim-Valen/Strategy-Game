dict = {}
dict["Dune"] = 9
dict["Niko"] = 1
dict["Harry"] = 5

lista = []


for title in dict:
    temp = []
    temp.append(title)
    temp.append(dict[title])
    lista.append(temp)

sorted_list = sorted(lista)

for list in sorted_list:
    print("{} {}".format(list[0], list[1]))
