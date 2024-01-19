
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
student_marks[query_name] = sum(student_marks[query_name])/3
print("%.2f" % student_marks[query_name])