def area_of_triangle(bottom, height):
    area = 0.5 * bottom * height
    print( "The area of a triangle with a bottom of", bottom, "and a height of", height,
    "is", area )
print(area_of_triangle(4.5, 1.0))

'''
this is using double print statements, which means the second print statement, the one outside the function, will print nothing because it
didn't receive any input.
'''