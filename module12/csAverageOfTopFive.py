"""
Understand
1. Find the answer test score of the two student ID's 
2. Take in 5 scores with integer divion to return averages

Plan
1. create a dictionary for students and answer
2. iterate thru with for loop
"""

import math

def csAverageOfTopFive(scores):

    students = {}
    answer = []
    
    for s in scores:
        if s[0] not in students:
            students[s[0]] = []
        students[s[0]].append(s[1])
        
    for stud in students:
        stud = students[stud].sort()
        
    for stu in students:
        if len(students[stu]) > 5:
            students[stu] = students[stu][-5:]
    
    for st in students:
        students[st] = math.floor(sum(students[st]) / len(students[st]))
    
    for key, value in students.items():
        answer.append([key, value])
        
    return answer
