#Write your code below this line 👇
def paint_calc(height, width, cover):
    surface_area = height*width
    number_of_cans = round(surface_area/5)
    remainder = (surface_area/5) - number_of_cans
    if remainder>= 0.1 and remainder < 0.5:
        number_of_cans+=1
    print(f"You'll need {number_of_cans} cans of paint.")





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

