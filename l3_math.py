print ("Введите радиус окружноости в см")
R = int
R = input()

if int(R) >= 0:

    L = int
    L = 2*3.14*int(R)
    print(str(L) + " сантиметров")
    Lm = int
    Lm = int(L)/100
    print(str(Lm) + " метров ")

    S = int
    S = 3.14*int(R)*int(R)
    print(str(S) + " сантиметров")
    Sm = int 
    Sm =  int(S)/100
    print(str(Sm) + " метров квадратных")    


    Sk = int 
    Sk = (2*int(R)/(2**0.5))
    print (str(Sk) + " сторона квадрата вписанного в окружность") 


    So = int 
    So = (int(R)*(3**0.5))
    print (str(So) + " сторона треугольника вписанного в окружность") 


    Ski = int 
    Ski = (2*int(R)*(3**0.5))
    print (str(Ski) + " сторона квадрата описанного около окружности") 


    Soi = int 
    Soi = (2*int(R))
    print (str(Soi) + " сторона треугольника описанного около окружности") 



    Sм = int 
    Sм = (2*((int(R)/3)**0.5))
    print (str(Sм) + " сторона Восьмиугольника вписанного в окружность") 

else:
    print("неправидьное значение")