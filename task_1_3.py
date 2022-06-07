numbers=range(1,101)
for number in numbers:
    if 0<number<=10 or number>20:
        if number%10==1:
            print(number, "процент")
        elif number%10==2:
            print(number, "процента")
        elif number%10==3:
            print(number, "процента")
        elif number%10==4:
            print(number, "процента")
        else:
            print(number, "процентов")
    else:
        print(number, "процентов")