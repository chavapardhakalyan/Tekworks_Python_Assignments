def convert_distance(feet):
    inches = feet * 12
    yards = feet / 3
    miles = feet / 5280
    print("Distance in feet : " + str(feet))
    print("Distance in inches : " + str(inches))
    print("Distance in yards : " + str(yards))
    print("Distance in miles : " + str(miles))


feet = float(input("Enter the distance in feet: "))
convert_distance(feet)
