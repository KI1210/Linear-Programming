from scipy.optimize import linprog

# Objective function
c = [-100000, -60000, -110000]*5

# Inequality constraints
A_ineq = ([
    [1]*3+[0]*12,
    [0]*3+[1]*3+[0]*9,
    [0]*6+[1]*3+[0]*6,
    [0]*9+[1]*3+[0]*3,
    [0]*12+[1]*3,
    [1.6, 2.9, 3.5]+[0]*12,
    [0]*3+[1.6, 2.9, 3.5]+[0]*9,
    [0]*6+[1.6, 2.9, 3.5]+[0]*6,
    [0]*9+[1.6, 2.9, 3.5]+[0]*3,
    [0]*12+[1.6, 2.9, 3.5],
    [1, 0, 0]*5,
    [0, 1, 0]*5,
    [0, 0, 1]*5
])

b_ineq = ([2000, 2300, 600, 1100, 500, 3200, 3400,
          800, 500, 600, 110000, 1800, 2200])

# Bounds
bound = [(0, float('inf'))]

print(c, A_ineq, b_ineq, bound*15, sep="\n")

# Solve
res = linprog(c=c, A_ub=A_ineq, b_ub=b_ineq, bounds=bound*15)

print("Optimum Value :", -1 * res.fun)  # Get the maximum value
print("Solution : ", res.x)
