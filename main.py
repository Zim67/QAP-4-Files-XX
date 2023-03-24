# Created On: March 20th, 2023
# Author: Zimuzo Akanne

import datetime

# read default values from file
with open('OSICDef.dat', 'r') as f:
    # Read the first line of the file and convert it to an integer
    POLICY_NUMBER = int(f.readline().strip())
    BASIC_PREMIUM = float(f.readline().strip())
    DISCOUNT = float(f.readline().strip())
    LIABILITY_COST = float(f.readline().strip())
    GLASS_COST = float(f.readline().strip())
    LOANER_COST = float(f.readline().strip())
    HST_RATE = float(f.readline().strip())
    PROCESSING_FEE = float(f.readline().strip())


# list of valid provinces
provinces = ['NL', 'PE', 'NS', 'NB', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU']

while True:
    # get customer information
    print('\nEnter customer information:')
    while True:
        first_name = input('First name: ').title()
        if first_name == "":
            print("The first name cannot be blank try again ")
        else:
            break

    while True:
         last_name = input('Last name: ').title()
         if last_name =="":
             print("The last name cannot be blank try again")
         else:
             break

    while True:
         address = input('Address: ')
         if address == "":
             print('Invalid address. Please enter a Valid address')
         else:
             break

    while True:
          city = input('City: ').title()
          if city == "":
              print("The city name cannot be blank try again ")
          else:
              break

    while True:
        province = input('Province: ').upper()
        if province not in provinces:
            print('Invalid province. Please enter a province')
        else:
            break

    while True:
        postal_code = input('Postal code: ')
        if postal_code == "":
            print('Invalid postal code. please enter a valid postal code in the format A1A 1A1')
        else:
             break

    while True:
        phone_number = input('Phone number: ')
        if phone_number == "":
            print('Invalid phone number. please enter a valid phone number in the format xxx-xxx-xxx')
        else:
            break


 # get car information
    num_cars = int(input('\nNumber of cars: '))
    while True:
        extra_cost = 0
        liability_option = input('Extra liability coverage (Y/N): ').upper()
        if liability_option == "":
            print("cannot be blank")
        elif liability_option == "Y":
            extra_cost += LIABILITY_COST
            break
        elif liability_option == "N":
            break
        else:
            print("Please enter Y or N")

    while True:
        glass_option = input('Glass coverage (Y/N): ').upper()
        if glass_option == "":
            print("cannot be blank")
        elif glass_option == "Y":
            extra_cost += GLASS_COST
            break
        elif glass_option == "N":
            break
        else:
            print("Please enter Y or N.")

    while True:
        loaner_option = input('Loaner car (Y/N): ').upper()
        if loaner_option == "":
            print("Please enter Y or N.")
        elif loaner_option == "Y":
            extra_cost += LOANER_COST
            break
        elif loaner_option == "N":
            break
        else:
            print("Please enter Y or N.")

    while True:
        payment_option = input('Payment method (F/M): ').upper()
        if payment_option == "":
            print("Please enter F or M.")
        elif payment_option == "F" or payment_option == "M":
            break
        else:
            print("Please enter F or M.")


# calculate insurance premium
if liability_option == 'Y':
    extra_cost += LIABILITY_COST
if glass_option == 'Y':
    extra_cost += GLASS_COST
if loaner_option == 'Y':
    extra_cost += LOANER_COST
total_cost = BASIC_PREMIUM + (DISCOUNT * (num_cars - 1)) + extra_cost
hst = HST_RATE * total_cost
total_cost += hst

# output results
print(f"Total cost for {num_cars} cars with extra coverage options:")
print(f"Basic premium: {BASIC_PREMIUM}")
if liability_option == 'Y':
    print(f"Extra liability coverage: ${LIABILITY_COST}")
if glass_option == 'Y':
    print(f"Glass coverage: ${GLASS_COST}")
if loaner_option == 'Y':
    print(f"Loaner car: ${LOANER_COST}")
print(f"Discount: ${DISCOUNT * (num_cars - 1)}")
print(f"Subtotal: ${total_cost - hst:.2f}")
print(f"HST: ${hst:.2f}")
print(f"Total: ${total_cost:.2f}")
print(f"Payment method: {payment_option}")


# calculate monthly payment
if payment_option == 'M':
    total_cost += PROCESSING_FEE
    monthly_payment = total_cost / 8
else:
    monthly_payment = None

currentDate = datetime.datetime.now()

# display receipt
print('\n\n********** The One Stop Insurance Company **********')
print(f'Date:    {currentDate}')
print(f'Policy Number: {POLICY_NUMBER}')
print('Customer Information:')
print(f'   Name:        {first_name} {last_name}')
print(f'   Address:     {address}')
print(f'   City:        {city}')
print(f'   Province:    {province}')
print(f'   Postal Code: {postal_code}')
print(f'   Phone Number:{phone_number}')
print('Car Information:')
print(f'   Number of cars:              {num_cars}')
print(f'   Extra liability coverage:    {liability_option}')
print(f'   Glass coverage:              {glass_option}')
print(f'   Loaner car:                  {loaner_option}')
print('Payment Information:')
print(f'   Payment method:              {payment_option}')
print(f'   Total cost:                  ${total_cost:.2f}')
if monthly_payment is not None:
    print(f'   Monthly payment:             ${monthly_payment:.2f}')
print('\n\n')



