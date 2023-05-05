# Integral Calculator Using N Rectangles - Riemann Summ - Midpoint Sum

'''
Similar to left and right hand sums, midpoint sums are a way to approximate the area under a curve using rectangles.
The difference is that the height of each rectangle is calculated using the midpoint of the interval instead of the left or right bound.
'''

# Variables
a = 0 # Lower bound of the integral
b = 1 # Upper bound of the integral
n = 100_000 # Number of rectangles to use

# The function to calculate the area under the curve for.
def f(x):
    return x**2


# Integral Function

def integral(a, b, n):
    
    # Calculates the area under the curve f(x) from a to b using n rectangles.

    area = 0 # Area under the curve

    width = (b-a)/n # Width of each rectangle

    def x_i(i): # Calculates the x value of the ith rectangle
        return a + i * width
    
    for i in range(n): # Calculates the area of each rectangle and adds it to the total area
        area += width * f((x_i(i) + x_i(i+1))/2) # The height of each rectangle is the average of the left and right hand sums (midpoint sum)

    return area

# Output
print("\nThe area of f(x) in the interval [", a, ",", b, "] is approximately", integral(a, b, n), "using midpoint sum.\n")