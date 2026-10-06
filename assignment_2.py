# Assignment Name: Interactive Profile & Calculator
"""
Objective: Independently demonstrate Tuesday’s concepts without following a step-by-step solution.

Build one program: Personal Profile + Simple Calculation.

The program should ask the user for:
• name
• age
• city
• a numeric value relevant to the user (for example monthly allowance, weekly spending, or study
hours)
• another numeric value relevant to a calculation

Then the program must:
• store the information in variables
• use appropriate data types
• convert numeric input
• perform at least two calculations
• display a readable summary using f-strings
• include at least one comment
• use type() at least once during development/debugging
• be tested with at least three input sets
• be saved in a Git repository with at least three meaningful commits
• finish with a clean working tree after the final commit
"""
print("INTERACTIVE PROFILE & CALCULATOR")
# GETTING & CHECKING TYPE OF INPUT: name, age, city, study_hour, cost_per_hour
name = input("Enter your name: ")
print(type(name))
age = input("How old are you?: ")
print(type(age))
city = input("City of residence: ")
print(type(city))
study_hour = float(input("Hours of study: "))
print(type(study_hour))
cost_per_hour = 24.0
print(type(cost_per_hour))

# CALCULATION: COST OF READING A STUDY MATERIAL
cost_Of_reading = study_hour * cost_per_hour

# OUTPUT: READABLE SUMMARY USING f-STRING
print(
f"""
*******************************
STUDENT READING SESSION RECEIPT
*******************************
{name} a resident of {city} and a {age} years old.
Studied for {study_hour} hours.
At a cost of ${cost_per_hour} per hour.
Total cost of reading is: ${cost_Of_reading}
"""
)