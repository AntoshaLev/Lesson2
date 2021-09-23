# Задание  1

print(type(15 * 3))
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))


# Задание 2

def get_sign(x):
    if x[0] in '+-':
        return x[0]


arr = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0

while i < len(arr):
    sign = get_sign(arr[i])
    if arr[i].isdigit() or (sign and arr[i][1:].isdigit()):
        if sign:
            arr[i] = sign + arr[i][1:].zfill(2)
        else:
            arr[i] = arr[i].zfill(2)

        arr.insert(i, '"')
        arr.insert(i + 2, '"')
        i += 2

    i += 1

words = ' '.join(arr)

print(words)

# Задание 4

arr = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(arr)):
    arr[i].islower()
    my_list = len(arr)
    my_list1 = arr[i].split(" ")
    hm_indexes = len(my_list1) - 1
    my_name = my_list1[hm_indexes]
    name = my_name.lower().title()
    arr.append(name)
    print("Привет " + name + "!")

# Задание 5

shopping_list = [10.46, 123.33, 33.33, 46, 192.8, 14.88, 86.16, 98, 76.1, 44.66, 48.4, 47.47]
for prices in sorted(shopping_list)[::-1][:5]:
    r = int(prices)
    kk = (prices - int(prices)) * 100
    print(f'{r} руб {kk:02.0f} коп', end=",")
