print("Size of Pond")
print("------------")
width = input("Enter pond width(meters: ")
width = int(width)
length = int(input("Enter pond length(meters): "))
depth = float(input("Enter pond length(meters): "))
area = width * length
volume = area * depth
print(volume, "cubic meters of water")
print("\n")

print("Filling the pond")
print("----------------")
second = float(input("Enter liters per second: "))
hour = second * 3600
print(hour, "liters per hour")
day = hour*24
#convert liters/day to cubic meters per day (m^3=1000L)
day = day/1000
print(day,"cubic meters per day")
'''
The number of days to fill the pond is the volume of the pond, divided by the water flow in one day
'''
days = volume/day
#round the number to 2 decimal places
\days = round(days,2)

#convert the numbers of days to full days plus extra
full_days = int(day)
part_day = days - full_days
hour = part_day * 24
print("it will take", full_days,"days","=","hours,to fill the pond")
