class Student:
    stud_ID = 0
    stud_Name = ""


    def __init__(self,ID,name):
        self.ID = ID
        self.name = name

    def displayStudent(self):
            print("ID", self.ID, "Name: ", self.name)
   
