


def python():
    pythonFile = open("Python.txt","w")
    pythonDatabase = "studentDataBases = []"
    pythonFile.write(pythonDatabase+"\n")
    for studentDataBase in studentDataBases:
        pythonDatabase = "studentDataBases.append(Student('" + studentDataBase.firstName+"', '" + studentDataBase.lastName+"', '" + studentDataBase.roll+"', '" + studentDataBase.department+"', '" + studentDataBase.email+"', '" + studentDataBase.mobile+"', '" + studentDataBase.gender+"', '" + studentDataBase.district+"')"
        pythonFile.write(pythonDatabase+"\n")
    pythonFile.close()

def java():
    javaFile = open("Java.txt","w")
    javaDatabase = "Student [] students = new Student[100]"
    javaFile.write(javaDatabase+"\n")
    objectNumber = 0
    for studentDataBase in studentDataBases:
        javaDatabase = 'students['+str(objectNumber)+'] =new Student("' + studentDataBase.firstName+'", "' + studentDataBase.lastName+'", "' + studentDataBase.roll+'", "' + studentDataBase.department+'", "' + studentDataBase.email+'", "' + studentDataBase.mobile+'", "' + studentDataBase.gender+'", "' + studentDataBase.district+"')"
        javaFile.write(javaDatabase+"\n")
        objectNumber = objectNumber+1
    javaFile.close()



def cPlusPlus():
    cPlusPlusFile = open("C++.txt", "w")
    cPlusPlusDatabase = "Student students[100]"
    cPlusPlusFile.write(cPlusPlusDatabase + "\n")
    objectNumber = 0
    for studentDataBase in studentDataBases:
        cPlusPlusDatabase = 'students[' + str(
            objectNumber) + ']("' + studentDataBase.firstName + '", "' + studentDataBase.lastName + '", "' + studentDataBase.roll + '", "' + studentDataBase.department + '", "' + studentDataBase.email + '", "' + studentDataBase.mobile + '", "' + studentDataBase.gender + '", "' + studentDataBase.district + "')"
        cPlusPlusFile.write(cPlusPlusDatabase + "\n")
        objectNumber = objectNumber + 1
    cPlusPlusFile.close()

class Student:
    def __init__(self, firstName, lastName, roll, department, email, mobile, gender, district):
        self.firstName=firstName
        self.lastName=lastName
        self.roll = roll
        self.department = department
        self.email = email
        self.mobile = mobile
        self.gender = gender
        self.district = district




studentDataBases = []
studentDataBases.append(Student('Mehedi', 'Hasan', '01', 'Physics', 'mehedi-hasan01@gmail.com', '01931546247', 'Male', 'Faridpur'))
studentDataBases.append(Student('Afsana', 'Mimi', '42', 'Chemistry', 'afsana-mimi42@gmail.com', '01754862485', 'Female', 'Dhaka'))
studentDataBases.append(Student('Sakib', 'Rahman', '07', 'Math', 'sakib-rahman07@gmail.com', '01945778354', 'Male', 'Khulna'))
studentDataBases.append(Student('Sazzad', 'Hossain', '24', 'Math', 'sazzat-hossain24@gmail.com', '01672786858', 'Male', 'Rajbari'))
studentDataBases.append(Student('Topu', 'Hasan', '13', 'Chemistry', 'topu-hasan13@gmail.com', '01757835427', 'Male', 'Dinajpur'))
studentDataBases.append(Student('Mohammad', 'Jakir', '21', 'Zoology', 'mohammad-jakir21@gmail.com', '018754757293', 'Male', 'Rajshahi'))
studentDataBases.append(Student('Rahat', 'Islam', '17', 'English', 'rahat-islam17@gmail.com', '01575555678', 'Male', 'Tangail'))
studentDataBases.append(Student('Nusrat', 'Fatema', '08', 'Chemistry', 'nusrat-fatema08@gmail.com', '01975836895', 'Female', 'Coxs Bazar'))
studentDataBases.append(Student('Abid', 'Mahmud', '14', 'English', 'abid-mahmud14@gmail.com', '01687329835', 'Male', 'Norail'))
studentDataBases.append(Student('Syeda', 'Taslim', '11', 'Physics', 'syeda-taslim11@gmail.com', '01827435668', 'Female', 'Kishoreganj'))
studentDataBases.append(Student('Shahdat', 'Khan', '02', 'Zoology', 'shahdat-khan02@gmail.com', '01576390500', 'Male', 'Mymensingh'))

python()
java()
cPlusPlus()