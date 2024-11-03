#User Input
rows = int(input("Enter the number of rows: "))

#Number Tracking
num = 1

#Rows
for i in range(1, rows + 1):

    #Numbers Each Row
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    
    print()
