print("Fish Pond Model")
print("===============")
width = float(input("Enter your pond width: "))
lenght = float(input("Enter your pond lenght: "))
depth = float(input("Enter pond depth: "))
print("\n")
print("Results")
print("-------")
area = width * length
print(area, "square meters")

volume = area * depth
print(volume, "cubic meters of water")

fish = volume * 2
print("Number of fish: ", fish)
