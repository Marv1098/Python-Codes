def get_number(phone):
    phone = phone.upper()
    if phone == 'A' or phone == 'B' or phone == 'C':
        number = '2'
    elif phone == 'D' or phone == 'E' or phone == 'F':
        number = '3'
    elif phone == 'G' or phone == 'H' or phone == 'I':
        number = '4'
    elif phone == 'J' or phone == 'K' or phone == 'L':
        number = '5'
    elif phone == 'M' or phone == 'N' or phone == 'O':
        number = '6'
    elif phone == 'P' or phone == 'Q' or phone == 'R' or phone == 'S':
        number = '7'
    elif phone == 'T' or phone == 'U' or phone == 'V':
        number = '8'
    elif phone == 'W' or phone == 'X' or phone == 'Y' or phone == 'Z':
        number = '9'
    else:
        number = phone
    return number

def translate_number():
    phone_number = input("Enter a number: ")
    result = ''
    for char in phone_number:
        if char.isalpha():
            new_ch = get_number(char)
            result = result + new_ch
        else:
            result = result + char
    print(result)

def main():
    translate_number()

main()

