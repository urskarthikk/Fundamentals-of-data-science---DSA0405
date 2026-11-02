import numpy as np

student_scores = np.array([
    [85, 90, 78, 88],
    [92, 85, 80, 75],
    [78, 88, 92, 80],
    [90, 95, 85, 92]
])

subjects = ["Math", "Science", "English", "History"]

avg = np.mean(student_scores, axis=0)

print("Average marks of each subject:")
for i in range(4):
    print(subjects[i], ":", avg[i])

print("Highest average subject:", subjects[np.argmax(avg)])
