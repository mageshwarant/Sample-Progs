hrs = input("Enter Hours:")
rate = input("Enter rate per hour")
rate = float(rate)
h = float(hrs)
grosspay = 0

def computepay(h,r):
  grosspay = 0
  if(h > 40):
      grosspay = (h-40)*r*1.5
  else:
      grosspay = r * h + float(grosspay)
  return grosspay


# hrs = raw_input("Enter Hours:")
# rate = raw_input("Enter rate per hour")
# rate = float(rate)
# h = float(hrs)

p = computepay(hrs,rate)
print("Pay",p)