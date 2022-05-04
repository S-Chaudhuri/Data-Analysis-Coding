print("Enter a integer for a day in the week(0-6)!")
a = int(input())
print("Enter number of days after today.")
b = int(input())
d=b%7
week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(f'The day is { week[(a+d-1)%7]}')