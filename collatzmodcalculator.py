""" take number and set multiple if conditions
in the form of mod. Then plug in the equations
"""
import math

number = input("What number do you wan to test?")

# 21 42 84 168 336 672 1344
if number%3  == 0 and \
   number%7  == 0 and \
   number%21 == 0:
   print (((math.log(number)-math.log(21))/math.log(2)) + 7)
   print 1
# 75 150 300 600 1200 2400
elif number%3  == 0 and \
     number%5  == 0 and \
     number%15 == 0 and \
     number%25 == 0 and \
     number%75 == 0:

	 print (((math.log(number)-math.log(75))/math.log(2)) + 14)
	 print 2

#453 906 1812 3624 7248
elif number%3   == 0 and \
     number%2   == 0 and \
     number%151 == 0 and \
     number%453 == 0:

	 print (((math.log(number)-math.log(453))/math.log(2)) + 14)
	 print 3

# 909 1818 3636 7272
elif number%3   == 0 and \
     number%9   == 0 and \
     number%101 == 0 and \
     number%303 == 0 and\
     number%909 == 0 :

	 print (((math.log(number)-math.log(909))/math.log(2)) + 15)
	 print 4

#1365 2730 5460 10920
elif number%3    == 0 and \
     number%5    == 0 and \
     number%7    == 0 and \
     number%13   == 0 and \
     number%15   == 0 and \
     number%21   == 0 and \
     number%35   == 0 and \
     number%39   == 0 and \
     number%39   == 0 and \
     number%65   == 0 and \
     number%91   == 0 and \
     number%105  == 0 and \
     number%195  == 0 and \
     number%1365 == 0:
#there are missing mod455, mod 273
	 print (((math.log(number)-math.log(1365))/math.log(2)) + 12)
	 print 5

#3 6 12 24 48 96 192 384
elif number%3  == 0 and \
     number%2  == 0 and \
     number%12 == 0 and \
     number%4  == 0 and \
     number%1  == 0 and \
     number%6  == 0:

	 print (((math.log(number)-math.log(3))/math.log(2)) + 7)
	 print 6

#45 90 180
elif number%3  == 0 and \
     number%5  == 0 and \
     number%9  == 0 and \
     number%15 == 0 and \
     number%45 == 0:

	 print (((math.log(number)-math.log(45))/math.log(2)) + 16)
	 print 7

#69 138 276 552 1104
elif number%3  == 0 and \
     number%23 == 0 and \
     number%69 == 0:

	 print (((math.log(number)-math.log(69))/math.log(2)) + 14)
	 print 8

#15 30
elif number%3  == 0 and \
     number%5  == 0 and \
     number%15 == 0:

	 print (((math.log(number)-math.log(15))/math.log(2)) + 17)
	 print 9

#93 186
elif number%3  == 0 and \
     number%31 == 0 and \
     number%3  == 0 and \
     number%93 == 0 :

	 print (((math.log(number)-math.log(93))/math.log(2)) + 17)
	 print 10

#141 282 564 1128
elif number%3   == 0 and \
     number%47  == 0 and \
     number%141 == 0 :

	 print (((math.log(number)-math.log(141))/math.log(2)) + 15)
	 print 11

# 213 426 852 1704
elif number%3    == 0 and \
     number%71   == 0 and \
     number%213  == 0 :

	 print (((math.log(number)-math.log(213))/math.log(2)) + 13)
	 print 12

else:
	print "Pick different number."

