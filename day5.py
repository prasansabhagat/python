import random
#student_heights = [2, 34, 565, 332, 45, 44, 33]
#sum = 0
#for i in student_heights:
#    sum += i
#average = round(sum/7, 2)
#print(average)

#listt = input("Enter list of marks obtained by students: ").split()
#for n in range(0, len(listt)):
#    listt[n] = int(listt[n])
#max = 0
#for i in listt:
#    if i > max:
#        max = i
#print(max)

#for n in range(1, 100):
#    if n%3==0 and n%5==0:
#        print("FIZZBUZZ")
#    elif n%5 == 0:
#        print("BUZZ")
#    elif n%3 == 0:
#        print("FIZZ")
#    else: 
#        print(n)

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','2','3','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*','+','-','/']
print("Welcome to Python Password generator")
letters = int(input("How many letters you want?"))
numbers = int(input("How many numbers you want?"))
symbols = int(input("How many symbols do you want?"))
password = ""
for i in range(1, letters+1):
    password += random.choice(letter)
for i in range(1, numbers+1):
    password += random.choice(number)
for i in range(1, symbols+1):
    password += random.choice(symbol)
print("Your password is: " + password)

#29/07/21
#done