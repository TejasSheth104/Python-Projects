# currency convertor

def usd_inr(amount):
    converted = amount * 75.12
    return converted
def eur_inr(amount):
    converted = amount * 85.72
    return converted
def jpy_inr(amount):
    converted = amount * 0.70
    return converted
def chf_inr(amount):
    converted = amount * 79.48
    return converted
def gbp_inr(amount):
    converted = amount * 94.57
    return converted
def inr_usd(amount): 
    converted = amount * 0.013
    return converted
def inr_eur(amount):
    converted = amount * 0.012
    return converted
def inr_jpy(amount):
    converted = amount * 1.42
    return converted
def inr_chf(amount):
    converted = amount * 0.013
    return converted
def inr_gbp(amount): 
    converted = amount * 0.011
    return converted

def convertor():
    while True:
        print('\n0. Exit')
        print('1. From USD To INR')
        print('2. From EUR To INR')
        print('3. From JPY To INR')
        print('4. From CHF To INR')
        print('5. From GBP To INR')
        print('6. From INR To USD')
        print('7. From INR To EUR')
        print('8. From INR To JPY')
        print('9. From INR To CHF')
        print('10. From INR To GBP')
        option = int(input('Enter - '))
        if option > 10:
            print('INVALID INPUT.')
            continue
        if option == 0:
            print('Thank You.')
            break
        amount = float(input('Enter amount - '))
        if option == 1:
            output = usd_inr(amount)
            print('output is -', output)
        elif option == 2:
            output = eur_inr(amount)
            print('output is -', output)
        elif option == 3:
            output = jpy_inr(amount)
            print('output is -', output)
        elif option == 4:
            output = chf_inr(amount)
            print('output is -', output)
        elif option == 5:
            output = gbp_inr(amount)
            print('output is -', output)
        elif option == 6:
            output = inr_usd(amount)
            print('output is -', output)
        elif option == 7:
            output = inr_eur(amount)
            print('output is -', output)
        elif option == 8:
            output = inr_jpy(amount)
            print('output is -', output)
        elif option == 9:
            output = inr_chf(amount)
            print('output is -', output)
        elif option == 10:
            output = inr_gbp(amount)
            print('output is -', output)

convertor()
