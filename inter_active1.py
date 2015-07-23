import math

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)


def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))

print max_of_3(2, 4, 8)

p = False
q = False
print not (p or not q)

def do_stuff():
    print "Hello world"
    return "Is it over yet?"
    print "Goodbye cruel world!"
    
print do_stuff()

n = 123
print ((n - n % 10) % 100) / 10
print (n % 10) / 10
print (n % 100 - n % 10) / 10

# f(x) = -5 x5 + 69 x2 - 47
# print "math.pow(100, 2) : ", math.pow(100, 2) = 1000
def powers_fn( x ):
    return (( -5 * math.pow( x, 5 )) + 
            ( 69 * math.pow( x, 2 )) - 47 )

print powers_fn(0), powers_fn(1), powers_fn(2), powers_fn(3)

# FV = PV (1+rate)^periods 
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return ( present_value * math.pow(( 1 + rate_per_period ), periods))
    
    # Put your code here.

# print "$1000 at 2% compounded daily for 3 years yields $", 
#     future_value(1000, .02, 365, 3)
# future_value(500, .04, 10, 10) should return 745.317442824.
print future_value(500, .04, 10, 10), future_value(1000, .02, 365, 3)

# # Given the number of sides, n, and the length of each side, s
# # 0.25 * n s^2 / ta( pi / n)
def polygon_area( no_sides, len_sides ) :
    return ( 0.25 * no_sides * math.pow( len_sides, 2)) \
        / ( math.tan( math.pi / no_sides ))

# a regular polygon with 5 sides, each of length 7 inches, 
#     has area 84.3033926289
print polygon_area( 5, 7 )
#
# polygon with 7 sides each of length 3 
print polygon_area( 7, 3 )
