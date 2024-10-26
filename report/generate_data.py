import csv
from faker import Faker
import random

def generate_data(filename='database.csv', num_records=100):
    fake = Faker()
    departments = ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance', 'Support']

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Hiring Date', 'Department', 'Birthday'])

        for _ in range(num_records):
            name = fake.name()
            hiring_date = fake.date_between(start_date='-10y', end_date='today')
            department = random.choice(departments)
            birthday = fake.date_of_birth(minimum_age=22, maximum_age=65)

            writer.writerow([name, hiring_date, department, birthday])

if __name__ == '__main__':
    generate_data()
