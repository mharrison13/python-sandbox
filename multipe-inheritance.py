# """
# Modul, which implements the class CalendarClock.
# """
#
# from clock import Clock
# from calendar import Calendar
#
#
# class CalendarClock(Clock, Calendar):
#     """
#         The class CalendarClock implements a clock with integrated
#         calendar. It's a case of multiple inheritance, as it inherits
#         both from Clock and Calendar
#     """
#
#     def __init__(self,day, month, year, hour, minute, second):
#         Clock.__init__(self,hour, minute, second)
#         Calendar.__init__(self,day, month, year)
#
#
#     def tick(self):
#         """
#         advance the clock by one second
#         """
#         previous_hour = self._hours
#         Clock.tick(self)
#         if (self._hours < previous_hour):
#             self.advance()
#
#     def __str__(self):
#         return Calendar.__str__(self) + ", " + Clock.__str__(self)
#
#
# if __name__ == "__main__":
#     x = CalendarClock(31,12,2013,23,59,59)
#     print("One tick from ",x, end=" ")
#     x.tick()
#     print("to ", x)
#
#     x = CalendarClock(28,2,1900,23,59,59)
#     print("One tick from ",x, end=" ")
#     x.tick()
#     print("to ", x)
#
#     x = CalendarClock(28,2,2000,23,59,59)
#     print("One tick from ",x, end=" ")
#     x.tick()
#     print("to ", x)
#
#     x = CalendarClock(7,2,2013,13,55,40)
#     print("One tick from ",x, end=" ")
#     x.tick()
#     print("to ", x)

#
# Diamond Problem:
#
# class A:
#     def m(self):
#         print("m of A called")
#
#
# class B(A):
#     def m(self):
#         print("m of B called")
#         super().m()
#
#
# class C(A):
#     def m(self):
#         print("m of C called")
#         super().m()
#
#
# class D(B, C):
#     def m(self):
#         print("m of D called")
#         super().m()

# in python, use a super function to solve the problem. the super function uses MRO or method resolution order to pull from each class