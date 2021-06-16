#Space complexity

# num = int(input("Enter a number to check Even or odd: "))
# if num % 2 == 0:
#     print(num, "number is Even")
# else:
#     print(num, "That number is Odd..")
# ctrl + /

#now look at this:
num2 = 10
even = [False] * (num2+1)
for i in range(1, num2, 2):
    even[i] = True

print(even[8])
