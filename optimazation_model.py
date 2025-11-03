#Internship TASK-4 
# OPTIMIZATION MODEL 

# Step 1: Import necessary library
from pulp import LpMaximize, LpProblem, LpVariable, value

# Step 2: Create a Linear Programming problem
model = LpProblem(name="factory-production-optimization", sense=LpMaximize)

# Step 3: Define decision variables
# x = number of Product A units (must be >= 0)
# y = number of Product B units (must be >= 0)
x = LpVariable(name="Product_A", lowBound=0)
y = LpVariable(name="Product_B", lowBound=0)

# Step 4: Define the objective function
# Maximize profit = 40x + 30y
model += 40 * x + 30 * y, "Total_Profit"

# Step 5: Define the constraints
# 1. Labor hours constraint: 2x + y <= 100
model += (2 * x + 1 * y <= 100, "Labor_Constraint")

# 2. Material constraint: 3x + 2y <= 120
model += (3 * x + 2 * y <= 120, "Material_Constraint")

# Step 6: Solve the problem
model.solve()

# Step 7: Print the results
print("Status:", model.status)
print(f"Optimal number of Product A to produce: {x.value()}")
print(f"Optimal number of Product B to produce: {y.value()}")
print(f"Maximum Profit: ₹{value(model.objective)}")

# Step 8: Optional — Show all constraints results
print("\n--- Constraint details ---")
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
