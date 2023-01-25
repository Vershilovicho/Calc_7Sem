from logg import logging
from typing import Union


def check_in(data: list, count: str, real_im=0):
    while True:
        check = [float(i) if "." in i else int(i) for i in data if i.replace(
            ".", "", 1).replace("-", "", 1).isdigit()]
        if len(check) == 2:
            return check
        else:
            logging.warning(
                f"Incorrect data entered: '{data[0]}', '{data[1]}'!")
            print('Try again!')
            match count:
                case "1":
                    data = [input(f"Enter {i + 1} number: ") for i in range(2)]
                case "2":
                    match real_im:
                        case 0:
                            data = [input(f"Enter 1 real part: "), input(
                                f"Enter 1 imaginary number: ")]
                        case 1:
                            data = [input(f"Enter 2 real part: "), input(
                                f"Enter 2 imaginary number: ")]


def zero_real(data: str):
    while True:
        d = [float(i) if "." in i else int(i) for i in [data]
             if i.replace(".", "", 1).replace("-", "", 1).isdigit()]
        if not (d and d[0]):
            print('You can t divide by zero!Try again!')
            logging.warning(f"Incorrect data entered: '{data}'!")
            data = input(f"Enter 2 number: ")
        else:
            return d[0]


def zero_comp(data_1: Union[int, float], data_2: Union[int, float]):
    while True:
        try:
            data_1 / data_2
        except ZeroDivisionError:
            print(f'You can t divide by zero! Try again!')
            logging.warning(f"Incorrect data entered: '{data_2}'!")
            data_2 = complex(
                *check_in([input(f"Enter 2 real part: "), input(f"Enter 2 imaginary number: ")], "2", 1))
        else:
            return data_2


def check_in_one(data: list, count: str):
    while True:
        check = [float(i) if "." in i else int(i) for i in data if i.replace(".", "", 1).replace("-", "", 1).isdigit()]
        match count:
            case "1":
                if len(check) == 1:
                    return check[0]
                print('Try again!')
                logging.warning(f"Incorrect data entered: '{data[0]}'!")
                data = [input(f"Enter a number: ")]
            case "2":
                if len(check) == 2:
                    return check
                print('Try again!')
                logging.warning(
                    f"Incorrect data entered: '{data[0]}', '{data[1]}'!")
                data = [input(f"Enter real part: "), input(f"Enter imaginary number: ")]
