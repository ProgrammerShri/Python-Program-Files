import datetime
import calendar

year = int(input("Enter Year Between 1500 - 2200=  "))
month = int(input("Enter Month Between 1-12 =  "))
day =  int(input("Enter Date Between 1 -31  =  "))
div = year//400

''' ******************************Year Code**********************************'''

if year >1500 & year < 1599 & year >1900 & year < 1999:
    year_code = 0
    print("YC 0")
elif year >1600 & year < 1699 & year >2000 & year < 2099:
    year_code = 6
    print("YC 6")
elif year >1700 & year < 1799 & year >2100 & year < 2199:
    year_code = 4
    print("YC 4")
elif year > 1800 & year < 1899 & year > 2200 & year < 2299:
    year_code = 2
    print("YC 2")
else :
    print("Y"
          "ear Must Be 1500 to 2200")

''' ******************************Month Code**********************************'''

if month == 1 or 10 :
    month_code = 1
    print("MC 1")
elif month ==  2 or 3 or 11:
    month_code = 4
    print("MC 4")
elif month ==  4 or 7:
    month_code = 0
    print("MC 0")
elif month ==  5 :
    month_code = 2
    print("MC 2")
elif month ==  6:
    month_code = 5
    print("MC 5")
elif month ==  7:
    month_code = 3
    print("MC 3")
elif month ==  8 or 12:
    month_code = 6
    print("MC 6")
else :
    print("Month Must Have 1 - 12 ")

''' ******************************Main Formula**********************************'''

F  = (year+div+month_code+year_code+day)%7
print(year,div,month_code,year_code,day)

print(F)

''' ******************************Main Formula Condition Use **********************************'''

if month == 2 and  (year/400 == 0):
    F = F-1
else:
    F = F


''' ******************************Day Code**********************************'''

if F == 1:
    Ans = "Sunday"
elif  F == 2:
    Ans ="Monday"
elif  F == 3:
    Ans ="Tuesday"
elif  F == 4:
    Ans ="Wednesday"
elif  F == 5:
    Ans ="Thursday"
elif  F == 6:
    Ans ="Friday"
elif  F == 0 or 7:
    Ans ="Saturday"

print(Ans)
''' ******************************Print Result**********************************'''

print("Your Enter Day " + str(day) + " - " + str(month) + " - "+ str(year) + " is " + str(Ans))

