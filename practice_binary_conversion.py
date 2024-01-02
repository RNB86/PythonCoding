import random

def getUserChoice():
    """
        Get user choice to continue practicing or not.
    """
    print("Would you like to practice more? Enter you choice: 'Y/n' and 1/0, or hit 'Enter to continue...'")
    u_input = input().rstrip()

    if u_input.lower() == 'n' or u_input == '0':
        return False
    else:
        return True

def readAndValidateUserBinaryInput():

    while True:
        user_input = input().rstrip()
        try:
            if user_input.lower() == 'b':
                break
            user_input_int = int(user_input, 2)
            break
        except ValueError:
            print("Invalid binary input. Please enter a valid 8 digits binary string.")
    return user_input

def printResult(r_num,u_input):
    """
        Print the result of the user's input and the correct binary representation.
    """
    try:
        user_input_int = int(user_input, 2)
        print(f"User:   {user_input.zfill(8)} = {user_input_int}")
#        print(f"{bin(random_octet)} = {random_octet}")
        print(f"Answer: {bin(random_octet)[2:].zfill(8)} = {random_octet}")
    except ValueError:
        print("Invalid input. Please enter a valid binary string.")

if __name__ == '__main__':
    while True:
        user_choice = getUserChoice()
        if not (user_choice):
            break
        random_octet = random.randint(0, 255)
        print(f"What is the binary value of {random_octet}?")
        print("--------------------------------")
        print("| 128  64  32  16  8  4  2  1  |")
        print("--------------------------------")
        print("'b' to quit the program")
        user_input = readAndValidateUserBinaryInput()
        if user_input.lower() == 'b':
            print("Terminating the task.")
            print(f"The solutions:\n{bin(random_octet)[2:].zfill(8)} = {random_octet}")
            break
        printResult(random_octet,user_input)
        print("--------------------------------")
