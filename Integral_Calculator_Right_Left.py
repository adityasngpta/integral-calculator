# Integral Calculator Using N Rectangles - Riemann Summ - Right Hand Sum and Left Hand Sum

'''
As I continue to delve into the fascinating world of Calculus, I have come across an intriguing concept known as integration.
A useful way to approximate integration involves the use of rectangles. 
The program that I have created will estimate the area beneath a curve by utilizing n rectangles. 
While the precise calculation of the area beneath a curve requires the utilization of limits with infinite rectangles, I am still in the process of mastering this technique. 
Nonetheless, the program provides a reasonably accurate approximation. Furthermore, given that it is in the form of code, it can be conveniently scaled up to accommodate an increased number of rectangles.
'''

# Variables
a = 0 # Lower bound of the integral
b = 1 # Upper bound of the integral
n = 100_000 # Number of rectangles to use

# The function to calculate the area under the curve for.
def f(x):
    return x**2


# Integral Function

def integral(a, b, n, sum_direction): # sum_direction is True for right hand sun, False for left hand sum
    
    # Calculates the area under the curve f(x) from a to b using n rectangles.

    area = 0 # Area under the curve

    width = (b-a)/n # Width of each rectangle

    def x_i(i): # Calculates the x value of the ith rectangle
        if sum_direction:
            return a + (i+1) * width
        else:
            return a + i * width
    
    for i in range(n): # Calculates the area of each rectangle and adds it to the total area
        area += width * f(x_i(i))

    return area

# Output
print("\nThe area of f(x) in the interval [", a, ",", b, "] is between", integral(a, b, n, False), "(left hand sum) and", integral(a, b, n, True), "(right hand sum).\n")