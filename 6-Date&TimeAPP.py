from datetime import datetime, timedelta
import os

print ("Performed by 42 & 47")

def show_current_datetime() -> datetime:
    now= datetime.now()
    print(f"\nCurrent Date : {now.strftime('%d - %m - %Y \nCurrent Time : %H:%M:%S')}")

def calculate_age() -> datetime:
    birth1 = input("Enter 'Darshan's Birthdate (DD-MM-YYYY): ")
    birth2 = input("Enter 'Yuvraj's Birthdate  (DD-MM-YYYY): ")
    try:
        birth_date1 = datetime.strptime(birth1,"%d-%m-%Y")
        birth_date2 = datetime.strptime(birth2,"%d-%m-%Y")
        today = datetime.now()
        age_year1 = today.year - birth_date1.year - ((today.month,today.day) < (birth_date1.month,birth_date1.day))
        age_year2 = today.year - birth_date2.year - ((today.month,today.day) < (birth_date2.month,birth_date2.day))
        
        print( f"'Darshan's age is : {age_year1}")
        print( f"'Yuvraj's age is : {age_year2}")
        
    except ValueError:
        print("Error while calculating age")

def event_date():
    event_date = input("Enter event date (DD-MM-YYYY) : ")
    event_name = input("Enter Event Name : ")
    try:
        event_date = datetime.strptime(event_date,"%d-%m-%Y")
        today = datetime.now()
        if event_date > today :
            days_left = (event_date - today).days
            print(f"{days_left} days left for the event.")
        else:
            print(f"The {event_name} already passed .")
    except ValueError:
        print("Error while calculating days.")

def main():
    while True:
        print("\n----Date & Time Application----")
        print("1. Show current date & time")
        print("2. Calculate Age")
        print("3. Event Date")
        print("4. Exit")
        choice = input("Enter Your Choice : ")
        if choice == '1':
            show_current_datetime()
        elif choice == '2':
            calculate_age()
        elif choice == '3':
            event_date()
        elif choice == '4':
            break
        else:
            print("Invalid Choice ..!!")

if __name__ == "__main__":
    main()
