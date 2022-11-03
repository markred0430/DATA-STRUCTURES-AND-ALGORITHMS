#Assignment 1:
#Create a program that will print your nickname using only asterisk character (*)
#Your program should be uploaded to github before 9:00 pm

Nickname ="RED"
#Initiating nested list to store the values for the loops.
print_R = [["  " for i in range(7)] for j in range(7)]
print_E = [["  " for i in range(7)] for j in range(7)]
print_D = [["  " for i in range(7)] for j in range(7)]

#This is the code for the letter R. It uses nested for loops to execute stars.
for row in range(7):
    for col in range(7):
        if (col==0) or ((row==0 or row==3) and (col>0 and col<4)) or ((col==4) and (row>0 and row<3)) or (row-col==2):
            print_R[row] [col] = "*"
#Code for E
for row in range(7):
    for col in range(7):
        if (row==0 or row==6) or (col==0) or (row==3 and col!=4):
            print_E[row][col] = "*"
#Code for D
for row in range(7):
    for col in range(7):
        if ((row == 0 or row == 6) and (col<5)) or (col==0 or col==5) and (row>0 and row<6):
            print_D[row][col] = "*"

#Combining the letters side by side.
for i in range(7):
    for j in range(7):
        print(print_R[i][j], end="  ")
    print(end="    ")
    for j in range(7):
        print(print_E[i][j], end="  ")
    print(end="    ")
    for j in range(7):
        print(print_D[i][j], end="  ")
    print()