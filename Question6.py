# Question:-

# WAP to find factorial of number

# code:

# Here we ask the user to give a number.
num=int(input('Enter a number: '))

# Here we introduce a variable which shall store the factorial of the number
pro_num=1

# Now we use a 'for' loop. I have provided the lower limit as 1 and the upper limit as num+1, because upper value is not counted
for i in range(1,num+1):

    # This line of code tells python to multiply rpo_num i.e. 1 with each element 'i' of given range
    pro_num*=i
    # Now we simply print the numbers
    print(pro_num)

# No additional comments

# OUTPUT :-
# Enter a number: 4
# 1
# 2
# 6
# 24
