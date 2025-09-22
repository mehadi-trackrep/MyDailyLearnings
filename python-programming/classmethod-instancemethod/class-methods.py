"""

Instance Methods => Best for operations on instances of the class (objects).
Static Methods => Best for utility functions that do not need access to class data.
Class Methods => Best for class-level data or require access to the class itself.

"""

class Student:
    count = 0
    total_gpa = 0
    
    def __init__(self, name, GPA):
        self.name = name
        self.GPA = GPA
        Student.count += 1
        Student.total_gpa += GPA
    
    # INSTANCE METHOD
    def display(self):
        return f"Name: {self.name}, GPA: {self.GPA}"
    
    # CLASS METHOD (buit-in decorator)
    @classmethod
    def total_students(cls):
        return f"Total Students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    
    
# Creating instances
s1 = Student("Alice", 20)
s2 = Student("Bob", 22)
s3 = Student("Charlie", 23)
print(s1.display())  # Output: Name: Alice, GPA: 20
print(s2.display())  # Output: Name: Bob, GPA: 22
print(s3.display())  # Output: Name: Charlie, GPA: 23
print(Student.total_students())  # Output: Total Students: 3# Demonstrating the use of instance and class methods
print(Student.get_average_gpa())  # Output: Average GPA: 21.67