print("Введите первое число,действие и второе число")
a=int(inptut())
b=input()
c=int(input())
if b=="+":
	print(a+b)
if b=="-":
	print(a-b)
if b=="/":
	print(a/b)
if b=="*":
	print(a*b)
else:
	print("Не правильный ввод")