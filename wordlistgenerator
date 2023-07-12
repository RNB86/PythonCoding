# generate wordlist with dates in format ddmmyyyy

def write_file(my_text, filename):
    print(f'writing into the file {filename}')
    try:
        the_file = open(filename, "w")
    except Exception as e:
        print('An error occurred:', e)
        return
    # write file
    print("save to file")
    the_file.writelines(my_text)
    the_file.close()


def generate_numbers(n):
    numbers = []
    for i in range(n + 1):
        if i > 0:
            if i < 10:
                a = "0"
                numbers.append(a + str(i))
            else:
                numbers.append(str(i))
    return numbers


def generate_years(start, end):
    numbers = []
    for i in range(start, end):
        numbers.append(str(i))
    return numbers


txt = ""

print("This python script will generate wordlist with dates in format ddmmyyyy")

# constants
DAYS = 31
MONTHS = 12
START_YEAR = 2022
END_YEAR = 2023

for year in generate_years(START_YEAR, END_YEAR + 1):
    for month in generate_numbers(MONTHS):
        for day in generate_numbers(DAYS):
            txt += day + month + year + '\n'

my_filename = "wordlist" + str(DAYS) + str(MONTHS) + str(END_YEAR)
userinput = input("write to file? Y/N \n")

if userinput.lower() == 'y':
    write_file(txt, my_filename)
else:
    print(txt)
