import sys
try:
      7/0

except ArithmeticError as e:
      print e
      print sys.exc_type
      print 'This is an example of catching ArithmeticError'