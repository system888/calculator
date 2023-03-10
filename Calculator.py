operations = [
    ["ADDITION", "Addition", "addition", "ADD", "Add", "add", "+"],
    ["SUBTRACTION", "Subtrcation", "subtraction", "MINUS", "Minus", "minus", "-"],
    ["MULTIPLICATION", "Multiplication", "multiplication", "TIMES", "Times", "times", "x", "X"],
    ["DIVISION", "Division", "division", "÷"]
]

import time

def calculator():
    key = ""
    general_number = 0
    try:
        while key != "space":
            select = input("Select Operation: ")
            if select in operations[0]:
                print("...ADDITION...")
                add_num1 = int(input("Start With: "))
                general_number += add_num1
                try:
                    while key != "space":
                        add_num2 = int(input(f"Add Num ({str(general_number)}): "))
                        general_number += add_num2
                        if add_num2 == 000:
                            break
                except KeyboardInterrupt:
                    print("\nExiting Operation")
                    time.sleep(1.5)
                except ValueError:
                    time.sleep(1);print("Something Went Wrong")
                    time.sleep(1);print("Invalid Error")

            elif select in operations[1]:
                print("...SUBTRACTION...")
                sub_num1 = int(input("Start With: "))
                general_number -= sub_num1
                try:
                    while key != "space":
                        sub_num2 = int(input(f"Subtract Num ({str(general_number)}): "))
                        general_number -= sub_num2
                        if sub_num2 == 000:
                            break
                except KeyboardInterrupt:
                    print("\nExiting Operation")
                    time.sleep(1.5)
                except ValueError:
                    time.sleep(1);print("Something Went Wrong")
                    time.sleep(1);print("Invalid Error")

            elif select in operations[2]:
                print("...MULTIPLICATION...")
                mult_num1 = int(input("Start With: "))
                general_number *= mult_num1
                try:
                    while key != "space":
                        mult_num2 = int(input(f"Multiply Num ({str(general_number)}): "))
                        general_number *= mult_num2
                        if mult_num2 == 000:
                            break
                except KeyboardInterrupt:
                    print("\nExiting Operation")
                    time.sleep(1.5)
                except ValueError:
                    time.sleep(1);print("Something Went Wrong")
                    time.sleep(1);print("Invalid Error")
            
            elif select in operations[3]:
                print("...DIVISION...")
                div_num1 = int(input("Start With: "))
                general_number /= div_num1
                try:
                    while key != "space":
                        div_num2 = int(input(f"Divide Num ({str(general_number)}): "))
                        general_number /= div_num2
                        if div_num2 == 000:
                            break
                except KeyboardInterrupt:
                    print("\nExiting Operation")
                    time.sleep(1.5)
                except ValueError:
                    time.sleep(1);print("Something Went Wrong")
                    time.sleep(1);print("Invalid Input")
    except KeyboardInterrupt:
        print("\nCalculator Off")
        time.sleep(1.5)
    except ValueError:
        time.sleep(1);print("Something Went Wrong")
        time.sleep(1);print("Invalid Error")

print("Calculator On")
calculator()
