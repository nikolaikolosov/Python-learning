n = input("Введите число 1 для вызова первой функции: ")
if n == "1":
    def echo():
        print("Вызвана первая функция")
else:
    def echo():
        print("Вызвана вторая функция")
echo()