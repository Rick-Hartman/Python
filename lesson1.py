#Задание 1:

a = 7
b = 13
print("Переменные a и b - ", a, b)
string1 = input("Введите первую строку ")
number1 = int(input("Введите первое число "))
string2 = input("Введите вторую строку ")
number2 = int(input("Введите второе число "))
print("Введеные значения - %10s %5d %10s %5d" % (string1, number1, string2, number2))

#Задание 2:

time = int(input("Введи время в секундах: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Конвертация времени в секундах в формат чч:мм:сс   {hours:02} : {minutes:02} : {seconds:02}")

#Задание 3:

n = int(input("Введи число: "))
summa = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел n + nn + nnn - %d" % summa)

#Задание 4:

n = abs(int(input("Введите целое положительное число: ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе: ", max)
        break

#Задание 5:

profit = float(input("Введите доход компании: "))
costs = float(input("Введите расходы компании: "))
if profit > costs:
    print(f"Компания приносит доход. Рентабильность дохода составляет: {profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников компании: "))
    print(f"Доход в расчете на одного сторудника сотавил {profit / workers:.2f}")
elif profit == costs:
    print("Компания работает в ноль")
else:
    print("Доход компании убыточен")

#Задание 6:

a = int(input("Введи дистанцию пробежки первого дня в км "))
b = int(input("Введи общий желаемый результат в км "))
result_days = 1
while a < b:
    a *= 1.1
    result_days += 1
print(f"Вы достигнете требуемых показателей на {result_days}-й день")