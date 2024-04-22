from scipy.optimize import linprog

# Objective function
c = [-6, -14, -13]

# Inequality constraints
A_ineq = ([
    [0.5, 2, 1],
    [1, 2, 4]
])

b_ineq = ([24, 60])

# Bounds
bound = (0, float('inf'))

# Solve
res = linprog(c=c, A_ub=A_ineq, b_ub=b_ineq, bounds=(bound, bound, bound))

print("Optimum Value :", res.fun)
print("Solution : ", res.x)
