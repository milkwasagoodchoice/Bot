import csv
import sys
from datetime import datetime

MONTHS = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4,
    'may': 5, 'june': 6, 'july': 7, 'august': 8,
    'september': 9, 'october': 10, 'november': 11, 'december': 12
}


def generate_report(filename, month_name):
    month = MONTHS.get(month_name.lower())

    if not month:
        print(f"Error: Invalid month '{month_name}'")
        return

    birthdays_by_dept = {}
    anniversaries_by_dept = {}
    total_birthdays = 0
    total_anniversaries = 0

    print(f"Reading file: {filename}")

    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)

            print(f"CSV Header: {reader.fieldnames}")

            for row in reader:
                print(f"Processing row: {row}")

                try:
                    birthday_month = datetime.strptime(row['Birthday'], "%Y-%m-%d").month
                    hiring_month = datetime.strptime(row['Hiring Date'], "%Y-%m-%d").month
                except ValueError as e:
                    print(f"Error parsing date: {e}")
                    continue

                department = row['Department']

                if birthday_month == month:
                    total_birthdays += 1
                    if department in birthdays_by_dept:
                        birthdays_by_dept[department] += 1
                    else:
                        birthdays_by_dept[department] = 1

                if hiring_month == month:
                    total_anniversaries += 1
                    if department in anniversaries_by_dept:
                        anniversaries_by_dept[department] += 1
                    else:
                        anniversaries_by_dept[department] = 1

        print(f"Report for {month_name.capitalize()} generated")
        print("--- Birthdays ---")
        print(f"Total: {total_birthdays}")
        print("By department:")
        for dept, count in birthdays_by_dept.items():
            print(f"- {dept}: {count}")

        print("--- Anniversaries ---")
        print(f"Total: {total_anniversaries}")
        print("By department:")
        for dept, count in anniversaries_by_dept.items():
            print(f"- {dept}: {count}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python report.py <database.csv> <month>")
    else:
        filename = sys.argv[1]
        month = sys.argv[2]
        generate_report(filename, month)
