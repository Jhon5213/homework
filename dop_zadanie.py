students = {
    'Johnny': (sum([4, 5, 5, 2]) / len([4, 5, 5, 2])),
    'Bilbo': (sum([2, 2, 2, 3]) / len([2, 2, 2, 3])),
    'Steve': sum([5, 5, 5, 4, 5]) / len([5, 5, 5, 4, 5]),
    'Khendrik': sum([4, 4, 3]) / len([4, 4, 3]),
    'Aaron': sum([5, 3, 3, 5, 4]) / len([5, 3, 3, 5, 4])}

students = sorted(students.items(), key=lambda x: x[0])
sortdict = dict(students)
print(sortdict)

