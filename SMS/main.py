class Person:
    def __init__(self,name):
        self.name = name

    def get_role(self):
        return "Person"


class Student(Person):

    def __init__(self, name,roll_no,marks):
        super().__init__(name)
        self.roll_no = roll_no
        self.__marks = marks


    def get_role(self):
        return "Student"

    def get_marks(self):
        return self.__marks
    
    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif  self.__marks >= 75:
            return "B"
        elif  self.__marks >= 50:
            return "C"
        else:
            return "F"
        
    def display(self):
        print(f" Roll_No : {self.roll_no} \n Name: {self.name} \n Marks: {self.__marks} \n Grade: {self.calculate_grade()}")
        print("-" * 50)


class StudentManager():

    def __init__(self):
        self.students = []  #Initialize Student List one time ehile calling StudentManager Class
        

    def add_Student(self):      
        name = input("Enter your Name")
        roll_no = input("Enter your Roll Number")
        marks = int(input("Enter your Marks"))

        std_Obj = Student(name,roll_no,marks)        
        self.students.append(std_Obj)


    def getAllStudents(self):
        return self.students
    
    
    def display_all_Students(self):

        if not self.students:
            print("No Student Found")
        else:
            for student in self.students:
                student.display()

    def save_to_File(self):
        with  open("students.txt","w") as file:
            for student in self.students:
                file.write(f"{student.name}, {student.roll_no}, {student.get_marks()} \n")
            print("Students saved successfully")


    def load_From_File(self):
        try:

            with  open("students.txt","r") as file:
                self.students.clear()    

                for line in file.readlines():
                 name,roll_no,marks = line.strip().split(',')
                 self.students.append(Student(name,int(roll_no),int(marks)))
         
                print("Student Data Loaded From File Successfully")

        except FileNotFoundError:
            print("File Not Found")


    
def main():
        stdmgr = StudentManager()
        while True:

            print(fr"1: Add Student \n2: Display All Students \n3:Save Student to File \n4:Load Students from File \n5:Exit")

            choice = int(input("Enter your Choice"))

            if choice == 1:
                stdmgr.add_Student()
            elif choice == 2:
                stdmgr.display_all_Students()
            elif choice == 3:
                stdmgr.save_to_File()
            elif choice == 4:
                stdmgr.load_From_File()
            elif choice == 5:
                print("Exiting Program...")
                break
            else:
                print("Invalid Option Please try Again")


if __name__ == "__main__":
        main()  
