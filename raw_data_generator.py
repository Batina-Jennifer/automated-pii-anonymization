import pandas as pd  #Handles spreadsheet data. Turns raw data into DataFrame (structured table).
from faker import Faker #"Faker" is the generator engine inside the "faker" library that generates fake data. 
import random #Built-in lib to generate random numbers, used to create random data for the DataFrame.

#Initializing the Faker() engine and storing it in a variable called "fake_data".
fake_data = Faker()

NUM_ROWS = 30  #Number of records to generate.

print(f"Generating mock data for testing purposes with {NUM_ROWS} records...")

#Creating a dictionary called raw_data to hold the fake raw data(rows and columns). 
raw_data = {
    "User_Name": [fake_data.name() for name in range(NUM_ROWS)],
    "Password": [fake_data.password() for password in range(NUM_ROWS)],
    "Email_ID": [fake_data.email() for email in range(NUM_ROWS)],
    "Phone": [fake_data.phone_number() for phone in range(NUM_ROWS)],
    "Address": [fake_data.address() for address in range(NUM_ROWS)],
    "IP_Address": [fake_data.ipv4_private() for ip in range(NUM_ROWS)]
}

#Converting the dictionary called raw_data into a DataFrame (structured table) using pandas.
df = pd.DataFrame(raw_data)

#Exporting it to a physical CSV file called "raw_data.csv" on our PC without the index numbers.
df.to_csv("raw_data.csv", index=False) 

print(f"Success! Mock data generated and saved to 'raw_data.csv' with {NUM_ROWS} sensitive user records.")