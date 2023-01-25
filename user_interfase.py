from excep import *
from mod_calc import *
from logg import logging

type_dict = {"1": "rational", "2": "complex"}
operator = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "^", "6": "sqrt"}


def menu():
    while True:
        type_num = input(
            "Choose number set:  \n1 - rational\n2 - complex\n3 - exit\n")
        match type_num:
            case '1' | '2':
                menu_calc(type_num)
            case '3':
                logging.info("Stop program")
                break
            case _:
                logging.warning("Wrong item selected")
                print('The menu item is not recognized. Try again!')


def menu_calc(data_type):
    global operator
    sign = "/"
    while True:
        # first, second = check_in(input("Enter 1 number: "), input("Enter 2 number: "))
        op_num = (input(
            "Choose a math operation:\n1 - sum\n 2 - sub\n 3 - mul\n 4 - div\n 5 - pow\n 6 - sqrt\n 0 - exit\n "))
        if op_num.isdigit() and int(op_num) in range(1, 6):
            if data_type == "1":
                first, second = check_in(
                    [input(f"Enter {i + 1} number: ") for i in range(2)], data_type)
            elif data_type == "2":
                first, second = [complex(*check_in([input(f"Enter {i + 1} real part: "),
                                                    input(f"Enter {i + 1} imaginary number: ")], data_type, i))
                                 for i in range(2)]
        match op_num:
            case '1':
                result = sum_num(first, second)
            case '2':
                result = sub_num(first, second)
            case '3':
                result = mult_num(first, second)
            case '4':
                if data_type == "1":
                    second = zero_real(str(second))
                    op = input("Operations:\n"
                               "1 - '/'\n"
                               "2 - '//'\n"
                               "3 - '%'\n"
                               "4 - previous menu\n")
                    match op:
                        case "1":
                            result = div_num(first, second)
                        case "2":
                            result = int_num(first, second)
                        case "3":
                            result = percent_num(first, second)
                        case "4":
                            logging.info('Stop divisions menu')

                else:
                    second = zero_comp(first, second)
                    operator[op_num] = "/"
                if sign:
                    result = div_num(first, second)

            case '5':
                result = pow_num(first, second)
            case '6':
                second = ""
                if data_type == "1":
                    first = check_in_one([input(f"Enter a number: ")], data_type)
                else:
                    first = complex(*check_in_one([input(f"Enter real part: "),
                                                   input(f"Enter imaginary number: ")], data_type))
                result = pow_num(first)
                logging.info(f"Sqrt: {first} = {result}")
                

            case '0':
                logging.info('Stop calc menu')
                print()
                break
            case _:
                logging.warning("Wrong item selected.")
                print('wrong menu number')
                break
        print(result)
        logging.info(result)
