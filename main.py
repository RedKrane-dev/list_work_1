fruits_list = ['Яблоко', 'Банан', 'Киви', 'Апельсин', 'Груша']

def fruits_replacer(fruits):
    fruits[0] = 'Персик'
    fruits[-1] = 'Абрикос'
    return fruits

print(fruits_replacer(fruits_list))
