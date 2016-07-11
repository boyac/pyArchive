class JustCounter:
   __secretCount = 0 #__ two underscore mean private attribute and can't be accessed from outside
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
#print counter.__secretCount

print counter._JustCounter__secretCount
