from datetime import date
import time

while True:
    today = date.today()
    birthdate = date(int(input("Year: ")), int(input("Month: ")), int (input("Day: ")))
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    a = str(age)
    print("You are " + a + " years old." + "\n")
    time.sleep(1)
        
