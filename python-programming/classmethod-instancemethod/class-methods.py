class Student:
    count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1
    
    # INSTANCE METHOD
    def display(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    # CLASS METHOD
    @classmethod
    def total_students(cls):
        return f"Total Students: {cls.count}"
    
    
# Creating instances
s1 = Student("Alice", 20)
s2 = Student("Bob", 22)
s3 = Student("Charlie", 23)
print(s1.display())  # Output: Name: Alice, Age: 20
print(s2.display())  # Output: Name: Bob, Age: 22
print(s3.display())  # Output: Name: Charlie, Age: 23
print(Student.total_students())  # Output: Total Students: 3# Demonstrating the use of instance and class methods