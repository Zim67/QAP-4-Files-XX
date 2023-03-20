import datetime

# Get the current date in YYYY-MM-DD format
today = datetime.date.today().strftime("%Y-%m-%d")

# Example data to write to the file
policy_number = "1944"
first_name = "John"
last_name = "Smith"
address = "12 Main St."
city = "St. John's"
province = "NL"
postal_code = "A1A8H4"
phone_number = "123-123-1234"
num_cars = "2"
liability_option = "Y"
glass_option = "N"
loaner_option = "Y"
payment_method = "F"
total_premium = "1329.00"

# Open the file in append mode and write the data
with open("Policies.dat", "a") as f:
    f.write(f"{policy_number}, {today}, {first_name}, {last_name}, {address}, {city}, {province}, {postal_code}, {phone_number}, {num_cars}, {liability_option}, {glass_option}, {loaner_option}, {payment_method}, {total_premium}\n")

print("Data written to Policies.dat.")
