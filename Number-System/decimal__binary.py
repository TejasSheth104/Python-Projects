

def decimal_binary():
    while True:
        print('\nSELECT -')
        print('\t0.) Go Back.')
        print('\t1.) Demical => Binary')
        print('\t2.) Binary => Decimal')
        try:
            select = int(input('Enter - '))
        except:
            print('Invalid Input.. Try Again.')
            continue
        if 0 > select > 2:
            print('Out of Range.. Try Again')
            continue
        if select == 0:
            print('Thanks.\nBack to the Menu.')
            break
        if select == 1:  # decimal to binary.
            decimal_parts = list()
            print('Demical => Binary')
            decimal = input('Enter Decimal - ')
            print('DECIMAL - ', decimal)
            if not decimal.isalpha():
                if decimal.isdigit():
                    decimal_parts.append(decimal)
                    print('ONLY INTEGER PART - ',decimal_parts[0])
                    answer = integer_calculation(int(decimal_parts[0]))
                elif type(decimal) == str:
                    decimal_parts = decimal.split('.')
                    integer_part = decimal_parts[0]
                    fraction_part = decimal_parts[1]
                    print('INTEGER PART - ',integer_part)
                    print('FRACTION PART - ',fraction_part)
                    answer1 = integer_calculation(int(integer_part))
                    answer2 = fraction_calculation(fraction_part)
                    answer = answer1 + '.' + answer2
                else:
                    print('InValid Type.. Try Again.')
                    continue
            else:
                print('DECIMAL - OOPSSSSS')
                continue

            print('DECIMAL', decimal, '-> BINARY', answer)


            




        #     # try:
        #     #     integer_part = int(decimal_parts[0])
        #     #     fraction_part = int(decimal_parts[1])
        #     # except:
        #     #     print('Error, Issue, Try Again')
        #     #     continue            

        # elif select == 2:
        #     print('Binary => Decimal')
        #     decimal = ''
        #     binary = float(input('Enter Decimal - '))
        #     print('BINARY - ',decimal)
        #     # result = int(decimal / 2)
        #     # print('Result - ',result)
        #     # remainder = int(decimal % 2)
        #     # print('Remainder - ',remainder)
        #     # while result != 0:
        #     #     binary = str(remainder) + binary
        #     #     print('Binary - ',binary)
        #     #     remainder = result % 2
        #     #     print('Remainder - ',remainder)
        #     #     result = int(result / 2)
        #     #     print('Result - ',result)
        #     # if result == 0:
        #     #     remainder = 1
        #     #     binary = str(remainder) + binary
        #     # print('DECIMAL', decimal, '-> BINARY', binary)
        #     # break


    
def integer_calculation(part_1):
    binary1 = ''
    binary_value = 2
    result = int(part_1 / binary_value)
    # print('Result - ',result)
    remainder = int(part_1 % binary_value)
    # print('Remainder - ',remainder)
    while result != 0:
        binary1 = str(remainder) + binary1
        # print('Binary - ',binary)
        remainder = result % binary_value
        # print('Remainder - ',remainder)
        result = int(result / binary_value)
        # print('Result - ',result)
    if result == 0:
        remainder = 1
        binary1 = str(remainder) + binary1
    return binary1

def fraction_calculation(part_2):
    let = '0.' + part_2
    let = float(let)
    binary2 = ''
    count, binary_value = 1, 2
    result = let
    while count <= 5:
        result = result * binary_value
        # print(result)
        convert_2_str = str(result)
        value = convert_2_str.split('.')
        binary2 = binary2 + value[0]
        # print(binary2)
        if value[0] == '1':
            # print(value[0])
            result = '0.' + value[1]
            result = float(result)
        count += 1
    return binary2