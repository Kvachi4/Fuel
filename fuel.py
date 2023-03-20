while True:
    try:  
        fraction = input("Fraction: ").split('/')
        number1 = int(fraction[0])
        number2 = int(fraction[1])
        if number1 < number2:
            percent = (number1 /number2 ) * 100
        else:
            continue
    except ValueError:
        pass
    except ZeroDivisionError:
        pass  
    else:
        break
    
    
if number1 == number2:
    print("F")
elif number1 == 0 and number2 == 1:
    print("E")
else:
    print(f"{round(percent)}%")