import math
# from sympy import Eq, solve
# from sympy.abc import w, x, y, z
# theta = math.atan2(-4, 0) * 180/pi
# print(theta)



# def quad(a,b,c):
#     dscrmnnt = math.pow(b,2) - 4*a*c
#     if dscrmnnt < 0: 
#         print("no real solutions")
#         return None

#     sol_1 = (-b + math.sqrt(dscrmnnt))/(2*a)
#     sol_2 = (-b - math.sqrt(dscrmnnt))/(2*a)
    
# #     # return sol_1, sol_2
# sol = solve([ Eq(x + 4*y, 13),
#               Eq(2*x + y, 5),
# ])
# print(sol)
# print({ s:sol[s].evalf() for s in sol })

def simul(a1, b1, c1, a2, b2, c2):
    """
    this solves the simul equations of the form:
    a_1x + b_1y = c_1
    a_2x + b_2y = c_2
    """
    # write y in terms of x then solve for y.
    """
    y = (c1- a1x)/b1
    a2x + b_2 ((c1-a1x)/b1) = c2
    b1*a2x + b2*c1 -b2*a1x = b1*c2
    x (b1*a2 - b2*a1) = b1*c2 -b2*c1
    """
    # exp1 = b1*a2 - b2*a1
    # exp2 = b1*c2 - b2*c1
    # x = exp1/exp2
    # exp3 = c1 - a1*x
    # y = exp3/b1
    x = (b1*a2 - b2*a1)/(b1*c2 - b2*c1)
    y = (c1 - a1*x)/b1

    return x, y

def dot(v, u):
    """v and u are vectors. v and u -> list"""
    vx, vy = v[0], v[1]
    ux, uy = u[0], u[1]
    dotproduct = vx*ux + vy*uy
    return dotproduct
# solution = simul(1, 4, 13, 2, 1, 5)

# print(solution)
