import datetime

# read default values from file
with open('Insurance.dat', 'r') as f:
    # Read the first line of the file and convert it to an integer
    policy_number = int(f.readline())
    basic_premium = float(f.readline())
    discount = float(f.readline())
    liability_cost = float(f.readline())
    glass_cost = float(f.readline())
    loaner_cost = float(f.readline())
    hst_rate = float(f.readline())
    processing_fee = float(f.readline())

# list of valid provinces
valid_provinces = ['NL', 'PE', 'NS', 'NB', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU']

# keep track of policies
policies = []

while True:
    # get customer information
    print('\nEnter customer information:')
    first_name = input('First name: ').title()
    last_name = input('Last name: ').title()
    address = input('Address: ')
    city = input('City: ').title()
    province = input('Province: ').upper()
    while province not in valid_provinces:
        province = input('Invalid province. Please enter a valid province: ').upper()
    postal_code = input('Postal code: ')
    phone_number = input('Phone number: ')

    # get car information
    num_cars = int(input('\nNumber of cars: '))
    liability_option = input('Extra liability coverage (Y/N): ').upper()
    glass_option = input('Glass coverage (Y/N): ').upper()
    loaner_option = input('Loaner car (Y/N): ').upper()
    payment_option = input('Payment method (F/M): ').upper()

    # calculate insurance premium
    extra_cost = 0
    for i in range(num_cars):
        if liability_option == 'Y':
            extra_cost += liability_cost
        if glass_option == 'Y':
            extra_cost += glass_cost
        if loaner_option == 'Y':
            extra_cost += loaner_cost
    total_cost = basic_premium + (discount * (num_cars - 1)) + extra_cost
    hst = hst_rate * total_cost
    total_cost += hst

    # calculate monthly payment
    if payment_option == 'M':
        total_cost += processing_fee
        monthly_payment = total_cost / 8
    else:
        monthly_payment = None

    # display receipt
    print('\n\n********** The One Stop Insurance Company **********')
    print('Date:', datetime.date.today())
    print('Policy Number:', policy_number)
    print('Customer Information:')
    print('   Name:', first_name, last_name)
    print('   Address:', address)
    print('   City:', city)
    print('   Province:', province)
    print('   Postal Code:', postal_code)
    print('   Phone Number:', phone_number)
    print('Car Information:')
    print('   Number of cars:', num_cars)
    print('   Extra liability coverage:', liability_option)
    print('   Glass coverage:', glass_option)
    print('   Loaner car:', loaner_option)
    print('Payment Information:')
    print('   Payment method:', payment_option)
    print('   Total cost:', '$%.2f' % total_cost)
    if monthly_payment is not None:
        print('   Monthly payment:', '$%.2f' % monthly_payment)
    print('\n\n')

    # save policy information to file
    policies.append((policy_number, datetime.date.today(), first_name, last_name, address, city, province, postal_code,
                     (phone_number, num_cars, liability_option, glass_option)))
