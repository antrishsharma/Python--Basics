#Q3.) WAP to give sum of all number user enter until he eneter 0
num = int(input("enter number : ")) 
sum=0
while num != 0:
    num = int(input("enter number : "))
    sum = sum+ num
    
print(f"Sum of all entered number is : {sum}")    
