const customer1 = Object.create(MotelCustomer);
customer1.name = "John Smith";
customer1.birthDate = "1999-01-01";
customer1.gender = "Male";
customer1.roomPreferences = ["Single", "Non-Smoking", "Balcony"];
customer1.paymentMethod = "Credit Card";
customer1.mailingAddress = {
  street: "123 Main St",
  city: "Halifax",
  state: "NS",
  zipCode: "B3H 0A9"
};
customer1.phoneNumber = "555-555-5555";
customer1.checkInDateTime = {
  date: "2023-04-01",
  time: "14:00 PM"
};
customer1.checkOutDateTime = {
  date: "2023-04-04",
  time: "11:00 AM"
};

console.log(customer1.getAge()); // Output: 33
console.log(customer1.getDurationOfStay()); // Output: 4

getDurationOfStay() 
  const diff = this.checkOut.getTime() - this.checkIn.getTime();
  const duration = Math.ceil(diff / (1000 * 60 * 60 * 24));
  return duration;

getDescription() 
  const age = this.getAge();
  const durationOfStay = this.getDurationOfStay();
  const mailingAddress = `${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.state} ${this.mailingAddress.zip}`;
  const roomPreferences = this.roomPreferences.join(', ');

  return `Name: ${this.name}
          Age: ${age}
          Gender: ${this.gender}
          Room preferences: ${roomPreferences}
          Payment method: ${this.paymentMethod}
          Mailing address: ${mailingAddress}
          Phone number: ${this.phoneNumber}
          Check-in date: ${this.checkIn.toLocaleString()}
          Check-out date: ${this.checkOut.toLocaleString()}
          Duration of stay: ${durationOfStay} day(s).`;

