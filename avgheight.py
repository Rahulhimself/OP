#using for loops without using len function

student_heights = input("enter student heights :").split()
print(student_heights)
print(type(student_heights))
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
no_of_student = 0
for student in student_heights:
    no_of_student += 1
print(no_of_student)
avgheight = (total_height)/ (no_of_student)
print((avgheight))
