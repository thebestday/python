import csv



car_data = [['brand', 'price', 'year'], ['Volve', 1.5, 2017], ['Lada', 0.5, 2018], ['AUdi', 2.0, 2018]]



with open('example.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(car_data)
print('Writing complete!')



with open('example.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)



data_dict = [{'Name': 'Dima', 'age': 28}, {'Name': 'Kate', 'age': 29}, {'Name': 'Mike', 'age': 31}]

fieldnames = ['Name', 'age']



with open('example_1.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(data_dict)):
        writer.writerow(data_dict[i])




with open('example_1.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(dict(row))





import pandas as pd

DataFrame_from_csv = pd.read_csv('example_1.csv', sep='&')

print(type(DataFrame_from_csv))

print(DataFrame_from_csv)
