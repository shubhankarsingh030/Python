class Student:
    def __init__(self,roll_number,name,class_name):
        self.roll_number = roll_number
        self.name = name
        self.class_name =class_name
        self.marks = {}

    def add_marks(self,subject,marks):
        if subject in self.marks:
            print(f"{self.marks} already has marks of particular that {subject}")
        else:
            self.marks[subject] = marks

    def average_marks(self):
        if not self.marks:
            print("There are no available Marks")
        total_marks = sum(self.marks.values())
        avg_marks = total_marks/len(self.marks)
        return avg_marks
    def display_student_info(self):
        print(f"student Information")
        print(f"Roll Number : {self.roll_number}")
        print(f"name : {self.name}")
        print(f"class : {self.class_name}")
        print(f"marks : {self.marks}")
        print(f"Average Marks are :  {self.average_marks()}")

student1 = Student(14,"Shubhankar","12th")
student2 = Student(16,"Pankaj","10th")
student3 = Student(18,"Ayush","9th")
student4 = Student(20,"Tarush","7th")

student1.add_marks("English",89)
student1.add_marks("Hindi",95)

student2.add_marks("English",75)
student2.add_marks("Hindi",89)

student3.add_marks("English",65)
student3.add_marks("Hindi",60)

student4.add_marks("English",80)
student4.add_marks("Hindi",90)

student1.display_student_info()
student2.display_student_info()
student3.display_student_info()
student4.display_student_info()