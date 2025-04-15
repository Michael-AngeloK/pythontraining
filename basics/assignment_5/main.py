# Assignment 5
import numpy as np

# Employee Details: Employee ID, Department, Number of Years with AtliQ
employee_details = np.array([
    [101, 'Sales', 3],
    [102, 'HR', 5],
    [103, 'IT', 2],
    [104, 'Sales', 8],
    [105, 'IT', 6],
    [106, 'HR', 4],
    [107, 'IT', 7],
    [108, 'Sales', 1],
    [109, 'HR', 3]
])

# Survey Results: Employee ID, Happiness Score (1-10)
survey_results = np.array([
    [101, 8],
    [102, 10],
    [103, 9],
    [104, 6],
    [105, 7],
    [106, 8],
    [107, 9],
    [108, 5],
    [109, 7]
])

employee_result = np.hstack((employee_details, survey_results))
# print(employee_result)y.

# for row in employee_result:
#     print(f"Employee ID: {row[0]}, department: {row[1]}")


happiness_score = employee_result[:,4].astype(int)
# print(happiness_score)

sorted_happiness_score = np.sort(happiness_score)
# print(sorted_happiness_score)

departments = employee_result[:,1]
# print(departments)

average_happiness_score = np.sum(happiness_score)/len(happiness_score)
# print(f"{average_happiness_score:.1f}")

unique_departments = np.unique(employee_result[:,1])
# print(unique_departments)

hr_happiness = employee_result[employee_result[:,1] == 'HR'][:,4].astype(float)
average_hr_happiness = np.average(hr_happiness)
print(average_hr_happiness)