# 1 Simple number tringle pattren rows = 6



# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop

#rows = 5
#for i in range(rows):       #nested loop    #NOTE-(if rows will be 5 then the printed results will go upto 4)
 #   for j in range(i):
  #      print(i, end=' ')  # new line after each row
   # print('')


#2  ASK THE USER to print the inverted pyramid numbers

# rows = 5
# b = 0
                                                            # reverse for loop from 5 to 0 #note :- In inverted pyramid in last row only one number is printed
# for i in range(rows, 0, -1):
    # b += 1
    # for j in range(1, i + 1):
        # print(b, end=' ')
    # print('\r')                             #  '\r' use for reverse loop



  #4 inverted pyramid numbers with decending numbers  

# rows = 8
# for i in range(rows, 0, -1):
    # num = i
    # for j in range(0, i):
        # print(num, end=' ')
    # print("\r")

# 5:- Inverted pyramid of same digit of numbers

#rows = 6
#num = rows
# reverse for loop
#for i in range(rows, 0, -1):
    #for j in range(0, i):
     #   print(num, end=' ')
    #print("\r")

   
# 6 :- ASK USER to print Reverse  pyramid of numbers pattern
#Note: It is a downward increment pattern where numbers get increased in each iteration.
#  At each row, the amount of number is equal to the current row number

#rows = 6
#for i in range(1, rows):
    #for j in range(i, 0, -1):
     #   print(j, end=' ')
    #print("")

# 7   inverted pyramid numbers with  half pyramid pattern

#rows = 6
#for i in range(rows, 0, -1):
 #   for j in range(0, i + 1):
  #      print(j, end=' ')
   # print("\r")



# 8 :- ASK the user to print the pyramid of number less than 10
# num = 1
# stop = 2
# rows = 3

# for i in range(rows):
    # for column in range(1, stop):
        # print(num, end=' ')
        # num += 1
    # print("")
    # stop += 2


# 9 :- reverse  pattern of number from 1-10    
# start = 1
# stop = 2
# current_num = stop
# for row in range(2, 6):
    # for col in range(start, stop):
        # current_num -= 1
        # print(current_num, end=' ')
    # print("")
    # start = stop
    # stop += row
    # current_num = stop


# 14 :-  Alternate pattern of numbers 


#rows = 7
#i = 1
#while i <= rows:
 #   j = 1
  #  while j <= i:
   #     print((i * 2 - 1), end=" ")
    #    j = j + 1
    #i = i + 1
    #print('')

# 17:- DOWNWARD triangle pattern of star   


rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")    
