def fruits_replacer(fruits):
    try:
        fruits[0], fruits[-1] = 'Персик', 'Абрикос'
        return fruits

    except IndexError:
        return 'Передан пустой список'

fruits_list = ['Яблоко', 'Банан', 'Киви', 'Апельсин', 'Груша']

print(fruits_replacer(fruits_list))
