# Learning:
# - How for loop works
# - range() function
# - while loop basics

# Program: Print numbers from 1 to 10

for i in range(1, 11):
    print(i)


# Program: Print table of a number
num=int(input("enter a number : "))
for i in range(1,11):
  print(f"{num} x {i} = {num*i}")

# Program: Print numbers using while loop
i=10
while i>=1:
  print(f"Number : {i}")
  i-=1

# Program: Print even numbers from 1 to 20
for i in range(1, 21):
    if i%2 ==0:
        print(f"Even Number: {i}")


