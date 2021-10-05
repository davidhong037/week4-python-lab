data = open('CupcakeInvoices.csv')

# # #Question 3
# for row in data:
#     print(row)
# # #Question 4
# for row in data:
#     line = row.split(',')
#     print(line[2])
# # #Question 5
# for row in data:
#     line = row.split(',')
#     total = int(line[3]) * float(line[4])
#     print(total)
# # #Question 6
# total = 0

# for row in data:
#     line = row.split(',')

#     total += (int(line[3]) * (float(line[4])))
#     rounded = round(total, 2)
#     print(rounded)
total_c = 0
total_v = 0
total_s = 0

for row in data:
    line = row.rstrip('\n').split(',')
    
    for value in line:
        if value == 'Strawberry':
            total_s += (int(line[3]) * (float(line[4])))
            rounded_s = round(total_s, 2)
        elif value == 'Vanilla':
            total_v += (int(line[3]) * (float(line[4])))
            rounded_v = round(total_v, 2)
        elif value == 'Chocolate':
            total_c += (int(line[3]) * (float(line[4])))
            rounded_c = round(total_c, 2)

print(rounded_s, rounded_v, rounded_c)
            

data.close()


from matplotlib import pyplot as plt

x_values = ['Chocolate', 'Vanilla', 'Strawberry']
y_values = [rounded_c, rounded_v, rounded_s]

plt.bar(x_values, y_values)
plt.show()
