while True:
    print("Калькуляторы:")
    print("1-калькулятор обычный")
    print("2-калькулятор площади")
    print("3-калькулятор ИМТ")
    calculator=int(input("Какой вам нужен калькулятор:"))
    if calculator == 1:
        a = int(input("Введите число a:"))
        operation = input('Введите тип операции (+,-,/,*,**):')
        b = int(input("Введите число b:"))
        if operation == '+':
            print(a + b)
            print()
        elif operation == '-':
            print(a - b)
            print()
        elif operation == '/':
             print(a / b)
             print()
        elif operation == '*':
             print(a * b)
             print()
        elif operation == '**':
            print(a ** b)
            print()
        else:
            print('Введён некорректный математический операнд!')
            print()

    elif calculator == 2:
        figura = str(input("Введите фигуру для расчетов : "))
        if figura =="Треугольник":
            Storon_A=int(input("Введите сторону A :"))
            Storon_B=int(input("Введите сторону B :"))
            Storon_C=int(input("Введите сторону C :"))
            Vesota_h = int(input("Введите высоту :"))
            Perim1 = Storon_A + Storon_B + Storon_C
            print("Периметр равен :",Perim1)
            Ploshad1=(Storon_A/2)*Vesota_h
            print("Площадь равна :", Ploshad1)
            print()
        elif figura == "Квадрат":
           Storon_A = int(input("Введите сторону A :"))
           Perim2 = Storon_A*4
           print("Периметр равен :",Perim2)
           Ploshad2 = Storon_A*Storon_A
           print("Площадь равна :", Ploshad2)
           print()
        elif figura == "Круг":
            Radius = int(input("Введите радиус :"))
            Perim3 = 2*(Radius*3.14159)
            print("Периметр равен :", Perim3)
            Ploshad3 = 3.14159*(Radius*Radius)
            print("Площадь равна :", Ploshad3)
            print()
        elif figura == "Прямоугольник":
            Storon_A = int(input("Введите сторону A :"))
            Storon_B = int(input("Введите сторону B :"))
            Perim4 = (Storon_A+Storon_B)*2
            print("Периметр равен :",Perim4)
            Ploshad4 = Storon_A*Storon_B
            print("Площадь равна :", Ploshad4)
            print()
        else:
            print("ХЗ")
            print()
    elif calculator == 3:
        ves = int(input("Введите свой вес в кг:"))
        vozrast = int(input("Введите свой возраст:"))
        rost = int(input("Введите свой рост в см:"))
        print("1.2  - Физ нагрузка отсутсвует или минимальная.")
        print("1.38 - Тренировки средней тяжести 3 раз в неделю. ")
        print("1.46 - Тренировки средней тяжести 5 раз в неделю.")
        print("1.55 - Интенсивные тринеровки 5 раз в неделю.")
        print("1.64 - Тренировки каждый день.")
        print("1.73 - Интенсивные тренировки каждый день или по 2 раз в день.")
        print("1.9  - Ежедневная физ нагрузка + физическая нагрузка.")
        aktivnost = float(input("Введите свой коэфицент активности:"))
        pol= str(input("Введите свой пол:"))
        IMT = 0
        if pol == "МУЖСКОЙ":
            if aktivnost == 1.2:
                DCI =(ves*10+rost*6.25-vozrast*5+5)*1.2
            elif aktivnost == 1.38:
                DCI =(ves*10+rost*6.25-vozrast*5+5)*1.38
            elif aktivnost == 1.46:
                DCI =(ves*10+rost*6.25-vozrast*5+5)*1.46
            elif aktivnost == 1.55:
                DCI =(ves*10+rost*6.25-vozrast*5+5)*1.55
            elif aktivnost == 1.64:
                DCI =(ves*10+rost*6.25-vozrast*5+5)*1.64
            elif aktivnost == 1.73:
                DCI =(ves*10+rost*6.25-vozrast*5+5)*1.73
            elif aktivnost == 1.9:
                DCI =(ves*10+rost*6.25-vozrast*5+5)*1.9
            else:
                print("ХЗ")
        elif pol == "ЖЕСНСКИЙ":
            if aktivnost == 1.2:
                DCI = (ves*10+rost*6.25-vozrast*5-161)*1.2
            elif aktivnost == 1.38:
                DCI =(ves*10+rost*6.25-vozrast*5-161)*1.38
            elif aktivnost == 1.46:
                DCI =(ves*10+rost*6.25-vozrast*5-161)*1.46
            elif aktivnost == 1.55:
                DCI =(ves*10+rost*6.25-vozrast*5-161)*1.55
            elif aktivnost == 1.64:
               DCI =(ves*10+rost*6.25-vozrast*5-161)*1.64
            elif aktivnost == 1.73:
                DCI =(ves*10+rost*6.25-vozrast*5-161)*1.73
            elif aktivnost == 1.9:
                DCI =(ves*10+rost*6.25-vozrast*5-161)*1.9
            else:
                print("ХЗ")
        else:
            print("ХЗ")
        IMT = IMT + ves / ((rost / 100) * (rost / 100)) // 1
        print("Ваша норма каллорий в день равна:",DCI,"калл.")
        print("Ваш индекс массы тела",IMT)
        if IMT <= 16:
            print("У вас выраженный дефицит массы тела")
            print()
        elif IMT >= 16 and IMT <= 18.5:
            print("У вас недостаточная (дефицит) масса тела")
            print()
        elif IMT >= 18.5 and IMT <= 25:
            print("У вас норма")
            print()
        elif IMT >= 25 and IMT <= 30:
            print("У вас избыточная масса тела (предожирение)")
            print()
        elif IMT >= 30 and IMT <= 35:
            print("У вас ожирение первой степени")
            print()
        elif IMT >= 35 and IMT <=40:
            print("У вас ожирение второй степени")
            print()
        elif IMT >= 40:
            print("У вас ожирение третьей степени (морбидное)")
            print()
        else:
            print("ХЗ")
            print()
    else:
        print("ХЗ")
        print()