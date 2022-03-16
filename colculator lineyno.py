print("                                   ")
print("калькулятор от 28 февраля года приветствует вас")
print ("доступны следующии опирации:")
print ("сложение +")
print ("вычитание -")
print ("деление /")
print ("возводения в степень ^")
print  ("извлечения квадратного корня sqrt")
print("                                   ")
print("                                   ")
print("   ")
f1=0   
def read_namber(): #функция  считывет данные из консоли и проверяет тип данных, есле это не число то "вежливо" просит ввести корректное значение fesf
     while True:
         try:
             x1=int(input())
             return x1 
         except ValueError:
            print("Введи  ЁБАНУЮ ЦИФРУ ДЕБИЛ! блять")
print ("введите первое число")
x=read_namber()
print ("введите знак операции") 
flag=0
while flag== 0:
    z= input()
    if z== '+' or z== '-' or z== '*'or z== '/' or z== 'sqrt' or z== '^':
        flag= 1 
        
    else:
        print ("введите знак операции из списка выше ")
        print("сука!")

print ("введите второе число") 
y= read_namber()
print ("            ") 
print ("            ") 
if z== '/':
    while y==0:
        print ("деление на 0 даёт бесконечность, введите другой делитель")
        y=int(input ())   
    r=x/y
    print (x,'/',y,"=",r)
if  z== '+':
    r=x+y
    print (x,'+',y,"=",r)
if  z=='-':
    r=x-y
    print (x,'-',y,"=",r)
if  z=='*':
    r=x*y
    print (x,'*',y,"=",r)
if  z=='sqrt':
    r=x**0.5
    print (x,'sqrt',y,"=",r)
if  z=='^':
    r=x**y
    print (x,'^',y,"=",r)
print ("stop")

    