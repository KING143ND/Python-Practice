
# class Solution:
#   def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
#     def isLeapYear(year: int) -> bool:
#       return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

#     week = ["Sunday", "Monday", "Tuesday",
#             "Wednesday", "Thursday", "Friday", "Saturday"]
#     days = [31, 29 if isLeapYear(
#         year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     count = 0

#     for i in range(1971, year):
#       count += 366 if i % 4 == 0 else 365
#     for i in range(month - 1):
#       count += days[i]
#     count += day

#     return week[(count + 4) % 7]

# emp1 = Solution()
# print(emp1)

# Python program to Find day of
# the week for a given date
import calendar

def findDay(date):
	day, month, year = (int(i) for i in date.split(' '))
	dayNumber = calendar.weekday(year, month, day)
	days =["Monday", "Tuesday", "Wednesday", "Thursday",
						"Sukrawaar", "Saturday", "Sunday"]
	return (days[dayNumber])

# Driver program
date = '15 07 2022'
print(findDay(date))

