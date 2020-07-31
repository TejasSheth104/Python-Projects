

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
        if select == 1:
            print('Demical => Binary')
            binary = ''
            decimal = input('Enter Decimal - ')
            decimal_parts = decimal.split('.')
            # try:
            #     integer_part = int(decimal_parts[0])
            #     fraction_part = int(decimal_parts[1])
            # except:
            #     print('Error, Issue, Try Again')
            #     continue
            integer_part = decimal_parts[0]
            fraction_part = decimal_parts[1]
            print('DECIMAL - ',decimal)
            print('INTEGER PART - ',integer_part)
            print('FRACTIoN PART - ',fraction_part)
            result = int(integer_part / 2)
            # print('Result - ',result)
            remainder = int(integer_part % 2)
            # print('Remainder - ',remainder)
            while result != 0:
                binary = str(remainder) + binary
                # print('Binary - ',binary)
                remainder = result % 2
                # print('Remainder - ',remainder)
                result = int(result / 2)
                # print('Result - ',result)
            if result == 0:
                remainder = 1
                binary = str(remainder) + binary
            print('DECIMAL', decimal, '-> BINARY', binary)
            break
        elif select == 2:
            print('Binary => Decimal')
            decimal = ''
            binary = float(input('Enter Decimal - '))
            print('BINARY - ',decimal)
            # result = int(decimal / 2)
            # print('Result - ',result)
            # remainder = int(decimal % 2)
            # print('Remainder - ',remainder)
            # while result != 0:
            #     binary = str(remainder) + binary
            #     print('Binary - ',binary)
            #     remainder = result % 2
            #     print('Remainder - ',remainder)
            #     result = int(result / 2)
            #     print('Result - ',result)
            # if result == 0:
            #     remainder = 1
            #     binary = str(remainder) + binary
            # print('DECIMAL', decimal, '-> BINARY', binary)
            # break


