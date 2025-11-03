# Optimization-Model
*COMPANY* : CODETECH IT SOLUTIONS

*NAME* : JAGAN PADHIARY

*INTERN ID* : CT04DR268

*DOMAIN* : DATA SCIENCE

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH KUMAR
# Optimization Model using Linear Programming

This project demonstrates how to use **Linear Programming (LP)** to solve an **optimization problem** for maximizing profit in a factory production scenario.  
It is implemented in Python using the **PuLP** library.

---

##  Project Overview

In this project, a factory produces **two products (A and B)** using limited resources such as labor and materials.  
The goal is to determine the **optimal number of units** of each product to produce in order to **maximize total profit**, while staying within given resource constraints.

---

##  Problem Formulation

### Objective Function:
Maximize Profit  
\[Z = 40x + 30y\]  
Where:  
- \( x \) = number of Product A units  
- \( y \) = number of Product B units  

### Subject to Constraints:
1. Labor Constraint:  
   \[2x + y \leq 100\]

2. Material Constraint:  
   \[ 3x + 2y \leq 120\]

3. Non-negativity Constraints:  
   \[x, y \geq 0\]

---

##  Features

 Uses **Linear Programming** with PuLP  
 Calculates the **optimal production quantity** for each product  
 Displays **maximum profit** and constraint details  
 Beginner-friendly with well-commented code  

---

##  Technologies Used

| Category | Tool/Library |
|-----------|--------------|
| Programming Language | Python |
| Optimization Library | PuLP |
| Environment | Jupyter Notebook / VS Code / Any IDE |

---

## Code Workflow

Step 1 — Import Librariespython
from pulp import LpMaximize, LpProblem, LpVariable, value

Step 2️ — Define the Problem
model = LpProblem(name="factory-production-optimization", sense=LpMaximize)

Step 3️ — Decision Variables
x = LpVariable(name="Product_A", lowBound=0)
y = LpVariable(name="Product_B", lowBound=0)

Step 4️ — Objective Function
model += 40 * x + 30 * y, "Total_Profit"

Step 5️ — Constraints
model += (2 * x + 1 * y <= 100, "Labor_Constraint")
model += (3 * x + 2 * y <= 120, "Material_Constraint")

Step 6️— Solve and Display Results
model.solve()
print(f"Optimal A: {x.value()}, Optimal B: {y.value()}")
print(f"Maximum Profit: ₹{value(model.objective)}")

## Sample Output
Status: Optimal
Optimal number of Product A to produce: 20.0
Optimal number of Product B to produce: 60.0
Maximum Profit: ₹2600.0

## Real-World Applications

Factory production planning

Resource allocation and scheduling

Supply chain optimization

Transportation and logistics planning

<img width="902" height="359" alt="Image" src="https://github.com/user-attachments/assets/2f56890e-6bc3-4500-859e-dba92e31e752" />
