""" Student.py

A class representing a student and their marks for courses

"""

class Student:

    courseMarks = {}
    name = ""
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark

    def average(self):
        markTotal = 0
        if self.courseMarks:
            for mark in self.courseMarks.values():
                markTotal += mark
            return markTotal / len(self.courseMarks.keys())
        return 0

if __name__ == "__main__":
    newStudent = Student("Bob", "Marley")
    print newStudent.name
    print newStudent.family
    newStudent.addCourseMark("Biology", 80)
    newStudent.addCourseMark("Chemistry", 90)
    newStudent.addCourseMark("English", 75)
    newStudent.addCourseMark("Math", 100)
    newStudent.addCourseMark("Biology", 80)
    for className in newStudent.courseMarks.keys():
        print("%s's mark in %s was %d" % (newStudent.name, className, newStudent.courseMarks[className]))
