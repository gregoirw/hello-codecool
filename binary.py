start=1
while start==1:
    while True:
        try:
            input_number = input("Enter positive number and choose number type (2 for binary, 10 for decimal): ")
            number=input_number.split()
            a=int(number[0])
            b=int(number[1])
            break
        except ValueError:
            print("No valid integer! Please try again ...")
            True
        except IndexError:
            print("Invalid input! Please try again ...")
            True
    a=int(number[0])
    b=int(number[1])
    number_bin=[]
    number_dec_final=[]
    number_power=[]
    number_dec=list(map(int, str(a)))
    number_dec_del=list(map(int, str(a)))
    potega = int(len(number_dec))

    while True:
        if a>0 and b == 10:
            value = int(a % 2)
            a= int(a / 2)
            number_bin.append(value)
        elif potega>0 and b == 2:
            power = pow(2,potega)
            number_power.append(power)
            potega -= 1
            del number_dec_del[0]
        else: break
    #print(number_bin)
    if b ==10:
        number_bin.reverse()
        for x in number_bin:
            print(x, end='')
        #print(number_bin)
        print(" 2 \n")
    elif b ==2:
        number_power.append(1)
        del number_power[0]
        for i in range(0, len(number_power)):
            number_dec_final.append(number_power[i]*number_dec[i])
        #print(number_power)
        #print(number_dec)
        print (sum(number_dec_final), " 10 \n")
    else:
        break
