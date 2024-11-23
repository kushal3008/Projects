import mysql.connector
db = mysql.connector.connect(host="localhost", user="root", passwd="Kushal3008@", database="Hospital")
mycursor = db.cursor()
def addPatient():
    name = str(input("Enter the name of patient:"))
    gender = str(input("Enter the gender of patient:"))
    age = int(input("Enter the age of patient:"))
    query = "insert into Patient(Name,Gender,Age) values(%s,%s,%s)"
    value = [name,gender,age]
    mycursor.execute(query,value)
    db.commit()
    print("Patient Added Successfully")
def viewPatient(c):
    query = "select * from patient"
    mycursor.execute(query)
    for i in mycursor:
        print(i)
def viewDoctor():
    query = "select * from doctors"
    mycursor.execute(query)
    for i in mycursor:
        print(i)
def DoctorbyID(d):
    ans = 0
    query = f"select * from Doctors where DoctorId = {d}"
    ans = mycursor.execute(query)
    mycursor.fetchall()
    if ans != 0:
        return True
    else:
        return False
def patientbyID(c):
    ans = 0
    query = f"select * from Patient where PatientId = {c}"
    ans = mycursor.execute(query)
    mycursor.fetchall()
    if ans != 0 :
        return True
    else:
        return False
def checkAvailability(docId,appDate):
    impQuery = 0
    query = f"select count(*) from appointment where Doctor_id = {docId} and AppointmentDate = {appDate}"
    impQuery = mycursor.execute(query)
    mycursor.fetchall()
    if impQuery:
        return False
    else:
        return True


def bookAppointment():
    patientid = int(input("Enter patient id:"))
    doctorid = int(input("Enter doctor id:"))
    appointmentdate = str(input("Enter appointment date(YYYY-MM-DD):"))
    y = patientbyID(patientid)
    z = DoctorbyID(doctorid)
    if y and z:
        if checkAvailability(doctorid,appointmentdate) == True:
            query = "insert into appointment(Patient_Id,Doctor_id,AppointmentDate) values(%s,%s,%s)"
            values = [patientid,doctorid,appointmentdate]
            mycursor.execute(query,values)
            db.commit()
            print("Appointment has been booked!!!")
        else:
            print("Doctor is not available on given date!!!")
    else:
        print("Such doctor or patient does not exist!!!")

while True:
    print("1.Add Patient")
    print("2.View Patient")
    print("3.View Doctor")
    print("4.Book Appointment")
    print("5.Exit")
    n = int(input("Enter a choice of operation you want to perform:"))
    if n > 5 or n < 1:
        print("!!!Enter a valid option!!!")
    else:
        match(n):
            case 1:addPatient()
            case 2:viewPatient(1)
            case 3:viewDoctor()
            case 4:bookAppointment()
            case 5:break
