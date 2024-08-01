year = int(input("please enter the year : "))
month = int(input("please enter the month : "))
if month < 12:
    def leapyear(year):
        if year % 4 == 0:
            if year % 100 ==0:
                if year % 400 ==0 :
                    print("its a year year")
                    daysinleapyear()
        else:
            print("not a leap year")
            daysinnormalyear()
    def daysinleapyear():
        listofdays = [31,29,31,30,31,30,31,31,30,31,30,31]
        if month == 2 and leapyear(year):
            print("29 days in a month")
        else:
            days = listofdays[month -1]
            print(days)
    def daysinnormalyear():
        listofdays = [31,28,31,30,31,30,31,31,30,31,30,31]
        days = listofdays[month -1]
        print(days)
    leapyear(year)
else:
    print("please enter a valid number between 1 and 12")
