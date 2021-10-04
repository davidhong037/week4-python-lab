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

# data.close()


from matplotlib import pyplot as plt

x_values = [1, 2, 3, 4]
y_values = [5, 4, 6, 2]

plt.bar(x_values, y_values)
plt.show()
