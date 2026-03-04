#Fibonacci Serisi
1, 1, 2, 3, 5, 8, 13, 21, 34

firstnumber = 0
secondnumber = 1

fibonacci = [firstnumber, secondnumber]

for i in range(10):
    firstnumber , secondnumber = secondnumber , firstnumber + secondnumber
    fibonacci.append(secondnumber)

print(fibonacci)
