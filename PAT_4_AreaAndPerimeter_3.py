class Circle:
    __pi = 3.141   # private variable for pi
    
    @classmethod
    def area(cls, radii_list):
        for radius in radii_list:
            area = cls.__pi * (radius ** 2)  # Accessing __pi using cls.__pi
            print("Area of circle with radius", radius, ":", area)

    @classmethod
    def perimeter(cls, radii_list):
        for radius in radii_list:
            perimeter = 2 * cls.__pi * radius  # Accessing __pi using cls.__pi
            print("Perimeter of circle with radius", radius, ":", perimeter)

# Given list of radii
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Calling class methods
Circle.area(radii_list)
Circle.perimeter(radii_list)





