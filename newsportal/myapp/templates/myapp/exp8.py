import json
import csv
import shutil

with open('data.json') as f:
    d = json.load(f)
    employees = d['data']

with open('employee_file.csv', mode='w', newline="") as csv_file:
    fieldnames = ['id', 'employee_name', 'employee_salary', 'employee_age']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for emp in employees:
        writer.writerow({
            'id': emp['id'],
            'employee_name': emp['employee_name'],
            'employee_salary': emp['employee_salary'],
            'employee_age': emp['employee_age']
        })
print("Data written to csv file successfully.\n")

print("Employee Data from CSV:")
with open('employee_file.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

updated_employees = []
with open('employee_file.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if int(row['employee_salary']) < 100000:
            row['employee_salary'] = str(int(row['employee_salary']) + 10000)
        updated_employees.append(row)

with open('employee_file.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(updated_employees)

print("\nUpdated Employee Data (after increment):")
with open('employee_file.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

shutil.copy('original_image.jpg', 'copy_image.jpg')
print("\nImage copied successfully.")
