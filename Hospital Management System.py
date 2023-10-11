#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Hospital:
    def __init__(self):
        self.patient_list=[['1','NURO','VED','18','MALE','101','SHELA','VEDANT'],]
        self.doctors_list=[['1','VEDANT','NURO','AHMEDABAD'],]
        self.appointment_list=[['1','ROHAN','1','VEDANT','1','01/05/2004','12:00','3:00'],]
        self.dept=["NURO",]
        self.doc=["VEDANT"]
        self.usr=["ved","vedant"]
        self.pas=["12345","12345"]
        self.total_user=len(self.usr)
        self.usr_falg=True
        self.log = False
        self.idd=0
        self.chk=0
        self.menu()
    def menu(self):
        print('''
        1. Administration Mode
        2. User Mode
        ''')
        panel_choice=int(input("Enter Your Mode :"))
        if panel_choice == 1 :
            self.admin_chk()
        elif panel_choice == 2:
            self.user()
        else:
            print("Enter Valid Choice!!")
            self.menu()
    def admin_chk(self):
        username=input("Enter Username :")
        password=input("Enter Password :") 
        for i in range(self.total_user):
            if(username == self.usr[i] and password == self.pas[i]):
                print("Successfully logedin!!")
                self.admin()
                self.log = True
        if self.log == False :
            print("Your Password Is Wrong!!")
            print("Enter 1. Main Menu\nEnter 2. Try Again!!")
            chs=int(input("Enter Your Choice :"))
            if chs == 1:
                self.menu()
            elif chs == 2:
                self.admin_chk()
            else:
                print("Wrong Choice!!")
                print("Going To Main Menu!!")
                self.menu()
    def admin(self):
        print("-----------------------------------------")
        print("| To manage patients Enter 1 		|\n| To manage doctors Enter 2	 	|\n| To manage appointments Enter 3 	|\n| To Add New Admin And Password Enter 4	|\n| To Back Enter 5			|")
        print("-----------------------------------------")
        admin_choice = int(input("Enter your choice : "))
        if admin_choice == 1:
            self.patients()
        elif admin_choice == 2:
            self.doctors()
        elif admin_choice == 3:
            self.appointments()
        elif admin_choice == 4:
            a_name = input("Enter Admin Name :")
            a_pass = input("Enter Admin Password :")
            self.usr.append(a_name)
            self.pas.append(a_pass)
            self.admin()
        elif admin_choice == 5:
            self.menu()
        else:
            print("Wrong Choice!!")
            print("Enter Again!!!")
            self.admin()
    def patients(self):
        print("-----------------------------------------")
        print("|To add new patient Enter 1	  	|")
        print("|To display patient Enter 2	  	|")
        print("|To delete patient data Enter 3		|")
        print("|To edit patient data Enter 4    	|")
        print("|To Back enter 5      			|")
        print("-----------------------------------------")
        patient_choice=int(input("Enter Choice :"))
        if patient_choice == 1:
            self.new_patient()
        elif patient_choice == 2:
            self.display_patient()
        elif patient_choice == 3:
            self.delete_patient()
        elif patient_choice == 4:
            self.edit_patient()
        elif patient_choice == 5:
            self.admin()
        else:
            print("Wrong Choice!!")
            print("Enter Again!!!")
            self.patients()
    def new_patient(self):
        check = False
        p_id=input("Enter Patient Id:")
        p_dept=input("Enter Patient Department:")
        p_name=input("Enter Patient Name:")
        p_age=input("Enter Patient Age:")
        p_gender=input("Enter Patient Gender:")
        p_roomnum=input("Enter Patient Room Number:")
        p_address=input("Enter Patient Address:")
        p_Doctor=input("Enter patient Case Heandiling Doctor Name:")
        new_patient=[p_id,p_dept,p_name,p_age,p_gender,p_roomnum,p_address,p_Doctor]
        self.patient_list.append(new_patient)
        for i in range(len(self.dept)):
            if p_dept == self.dept[i]:
                check = True
        if(check == False):
            self.dept.append(p_dept)
        else:
            check = False
        self.patients()
    def display_patient(self):
        patient_id=input("Enter Patient Id To Display:")
        for i in range(len(self.patient_list)):
            if patient_id == self.patient_list[i][0]:
                print("patient Id                    :",self.patient_list[i][0])
                print("patient Depertment            :",self.patient_list[i][1])
                print("patient name                  : ",self.patient_list[i][2])
                print("patient age                   : ",self.patient_list[i][3])
                print("patient gender                : ",self.patient_list[i][4])
                print("patient address               : ",self.patient_list[i][6])
                print("patient room number           : ",self.patient_list[i][5])
                print("patient is followed by doctor : ",self.patient_list[i][7])
                self.chk=1
        if self.chk == 0:
            print("Data Not Found")
        else:
            self.chk = 0
        self.patients()
    def delete_patient(self):
        patient_id=input("Enter Patient Id To Delete:")
        for i in range(len(self.patient_list)):
            if patient_id == self.patient_list[i][0]:
                del self.patient_list[i]
                self.chk=1
                print("Patient Detail Deleted Successfully!!")
        if self.chk == 0:
                print("Data Not Found")
        else:
            self.chk = 0
        self.patients()
    def edit_patient(self):
        patient_id=input("Enter Patient Id To Edit:")
        for i in range(len(self.patient_list)):
            if patient_id == self.patient_list[i][0]:
                while True:
                    print("------------------------------------------")
                    print("|To Edit pateint Department Enter 1 :    |")
                    print("|To Edit Doctor following case Enter 2 : |")
                    print("|To Edit pateint Name Enter 3 :          |")
                    print("|To Edit pateint Age Enter 4 :           |")
                    print("|To Edit pateint Gender Enter 5 :        |")
                    print("|To Edit pateint Address Enter 6 :       |")
                    print("|To Edit pateint RoomNumber Enter 7 :    |")
                    print("|To be Back Enter 8                      |")
                    print("-----------------------------------------")
                    Admin_choice = int(input("Enter your choice : "))
                    if Admin_choice == 1:
                        p_dept=input("Enter Patient New Depertment :")
                        self.patient_list[i][1]=p_dept
                        self.patients()
                    elif Admin_choice == 2:
                        p_Doctor=input("Enter Doctor New Name :")
                        self.patient_list[i][7]=p_Doctor
                        self.patients()
                    elif Admin_choice == 3:
                        p_name=input("Enter Pateint New Name :")
                        self.patient_list[i][2]=p_name
                        self.patients()
                    elif Admin_choice == 4:
                        p_age=input("Enter Pateint New Age :")
                        self.patient_list[i][3]=p_age
                        self.patients()
                    elif Admin_choice == 5:
                        p_gender=input("Enter Patient New Gender :")
                        self.patient_list[i][4]=p_gender
                        self.patients()
                    elif Admin_choice == 6:
                        p_add=input("Enter Patient New Address :")
                        self.patient_list[i][6]=p_add
                        self.patients()
                    elif Admin_choice == 7:
                        p_room=input("Enter New Room Number :")
                        self.patient_list[i][5]=p_room
                        self.patients()
                    elif Admin_choice == 8:
                        self.patients()
                    else:
                        print("Wrong Choice!!")
                        print("Enter Again!!!")
                        self.patients()
                    self.chk = 1
        if self.chk == 0:
            print("Data Not Found")
        else:
            self.chk = 0
        self.patients()
            
    def doctors(self):
        print("-----------------------------------------")
        print("|To add new doctor Enter 1              |")
        print("|To display doctor Enter 2              |")
        print("|To delete doctor data Enter 3          |")
        print("|To edit doctor data Enter 4            |")
        print("|To be back enter 5                     |")
        print("-----------------------------------------")
        Admin_choice = int(input("Enter your choice : "))
        if Admin_choice == 1:
            self.add_doctors()
        elif Admin_choice == 2:
            self.display_doctors()
        elif Admin_choice == 3:
            self.delete_doctors()
        elif Admin_choice == 4:
            self.edit_doctors()
        elif Admin_choice == 5:
            self.admin()
        else:
            print("Wrong Choice!!")
            print("Enter Again!!!")
            self.doctors()
    def add_doctors(self):
        check = False
        d_id=input("Enter Doctors id :")
        d_name=input("Enter Doctor Name :")
        d_dept=input("Enter Doctor Depertment :")
        d_add=input("Enter Doctor Address :")
        doctor=[d_id,d_name,d_dept,d_add]
        self.doctors_list.append(doctor)
        for i in range(len(self.dept)):
            if d_dept == self.dept[i]:
                check = True
        if(check == False):
            self.dept.append(d_dept)
        else:
            check = False
        for i in range(len(self.doc)):
            if d_name == self.doc[i]:
                check = True
        if(check == False):
            self.doc.append(d_name)
        else:
            check = False
        self.doctors()
    def display_doctors(self):
        d_id=input("Enter Doctor Id To Display :")
        for i in range(len(self.doctors_list)):
            if d_id == self.doctors_list[i][0]:
                print("Doctor ID          :",self.doctors_list[i][0])
                print("Doctor Name        :",self.doctors_list[i][1])
                print("Doctor Depertment  :",self.doctors_list[i][2])
                print("Doctor Address     :",self.doctors_list[i][3])
                self.chk = 1
        if self.chk == 0:
            print("Data Not Found")
        else:
            self.chk = 0
        self.doctors()
    def delete_doctors(self):
        d_id=input("Enter Doctor Id To Delete :")
        for i in range(len(self.doctors_list)):
            if d_id == self.doctors_list[i][0]:
                del self.doctors_list[i]
                self.chk = 1
                print("Doctor Detail Deleted Successfully!!")
        if self.chk == 0:
            print("Data Not Found")
        else:
            self.chk = 0
        self.doctors()
    def edit_doctors(self):
        d_id=input("Enter Doctor Id To Display :")
        for i in range(len(self.doctors_list)):
            if d_id == self.doctors_list[i][0]:
                print("-----------------------------------------")
                print("|To Edit doctor's department Enter 1    |")
                print("|To Edit doctor's name Enter 2          |")
                print("|To Edit doctor's address Enter 3       |")
                print("To be Back Enter B                      |")
                print("-----------------------------------------")
                Admin_choice = int(input("Enter your choice : "))
                if Admin_choice == 1:
                    d_dept=input("Enter Doctor New Depertment :")
                    self.doctors_list[i][2]=d_dept
                    self.doctors()
                elif Admin_choice == 2:
                    d_name=input("Enter Doctor New Name :")
                    self.doctors_list[i][1]=d_name
                    self.doctors()
                elif Admin_choice == 3:
                    d_add=input("Enter Doctor New Address :")
                    self.doctors_list[i][3]=d_add
                    self.doctors()
                elif Admin_choice == 4:
                    self.doctors()
                else:
                    print("Wrong Choice!!")
                    print("Enter Again!!!")
                    self.doctors()
                self.chk = 1
        if self.chk == 0:
            print("Data Not Found")
        else:
            self.chk = 0
        self.doctors()
    def appointments(self):
        print("-----------------------------------------")
        print("|To book an appointment Enter 1         |")
        print("|To edit an appointment Enter 2         |")
        print("|To cancel an appointment Enter 3       |")
        print("|To Display an appointment Enter 4      |")
        print("|To be back enter 5                     |")
        print("-----------------------------------------")
        Admin_choice = int(input("Enter your choice : "))
        if Admin_choice == 1:
            self.book_appointment()
        elif Admin_choice == 2 :
            self.edit_appointment()
        elif Admin_choice == 3 :
            self.cancel_appointment()
        elif Admin_choice == 4 :
            self.display_appointment()
        elif Admin_choice == 5:
            self.admin()
    def book_appointment(self):
        d_id=input("Enter Doctor Id :")
        for i in range(len(self.doctors_list)):
            if d_id == self.doctors_list[i][0]:
                print("1. New Patient\n2. Existing Patient\n3. Back")
                Admin_choice=int(input("Enter Your Choice :"))
                if Admin_choice == 1 :
                    self.new_patient()
                    p_id=input("Enter Patient Id To Book An Appointment :")
                    for i in range(len(self.patient_list)):
                        if p_id == self.patient_list[i][0]:
                            a_id=input("Enter Appoinment Id:")
                            a_date = input("Enter Date In dd/mm/yyyy Format :")
                            a_stime = input("Enter Start Time :")
                            a_etime = input("Enter End Time :")
                            appointment=[a_id,self.patient_list[i][2],p_id,self.doctors_list[i][1],d_id,a_date,a_stime,a_etime]
                            self.appointment_list.append(appointment)
                            self.chk = 1
                    if self.chk == 0:
                        print("Data Not Found")
                    else:
                        self.chk = 0
                    self.book_appointment()
                elif Admin_choice == 2 :
                    p_id=input("Enter Patient Id To Book An Appointment :")
                    for i in range(len(self.patient_list)):
                        if p_id == self.patient_list[i][0]:
                            a_id=input("Enter Appoinment Id:")
                            a_date = input("Enter Date In dd/mm/yyyy Format :")
                            a_stime = input("Enter Start Time :")
                            a_etime = input("Enter End Time :")
                            appointment=[a_id,self.patient_list[i][2],p_id,self.doctors_list[i][1],d_id,a_date,a_stime,a_etime]
                            self.appointment_list.append(appointment)
                            self.chk = 1
                    if self.chk == 0:
                        print("Data Not Found")
                    else:
                        self.chk = 0
                    self.book_appointment()
                elif Admin_choice == 3 :
                    self.appointments()
                else:
                    print("Wrong Choice!!")
                    self.book_appointment()
    def edit_appointment(self):
        a_id=input("Enter Appointment Id :")
        for i in range(len(self.appointment_list)):
            if a_id == self.appointment_list[i][0]:
                a_date = input("Enter New Date In dd/mm/yyyy Format :")
                a_stime=input("Enter New Start Time Of Appointment :")
                a_etime=input("Enter New End Time Of Appointment :")
                self.appointment_list[i][5]=a_date
                self.appointment_list[i][6]=a_stime
                self.appointment_list[i][7]=a_etime
                self.chk = 1
        if self.chk == 0:
            print("Data Not Found")
        else:
            self.chk = 0
        self.appointments()
    def cancel_appointment(self):
        a_id=input("Enter Appointment Id :")
        for i in range(len(self.appointment_list)):
            if a_id == self.appointment_list[i][0]:
                del self.appointment_list[i]
                print(f"Appointment With Id {self.appointment_list[i][0]} Is Deleted Successfully !!")
                self.chk = 1
        if self.chk == 0:
            print("Data Not Found")
        else:
            self.chk = 0
        self.appointments()
    def display_appointment(self):
        a_id=input("Enter Appointment Id To Display :")
        for i in range(len(self.appointment_list)):
            if a_id == self.appointment_list[i][0]:
                print("Appointment Id                   :",self.appointment_list[i][0])
                print("Appointment Patient Name         :",self.appointment_list[i][1])
                print("Appointment Patient Id           :",self.appointment_list[i][2])
                print("Appointment Doctor Name          :",self.appointment_list[i][3])
                print("Appointment Doctor Id            :",self.appointment_list[i][4])
                print("Appointment Date                 :",self.appointment_list[i][5])
                print("Appointment Session Start Time   :",self.appointment_list[i][6])
                print("Appointment Session End Time     :",self.appointment_list[i][7])
                self.chk = 1
        if self.chk == 0:
            print("Data Not Found")
        else:
            self.chk = 0
        self.appointments()

    def usr_chk(self):
        u_id=input("Enter Your Patient Id :")
        for i in range(len(self.patient_list)):
            if u_id == self.patient_list[i][0]:
                print("-------------------------------------------------")
                print(f"| Welcome Back {self.patient_list[i][2]} !!                      |")
                print("-------------------------------------------------")
                self.idd=i
                self.chk = 1
        if self.chk == 0:
            print("Data Not Found")
        else:
            self.chk = 0

    def user(self):
        print("-------------------------------------------------")
        print("|To View Your Appointments Enter 1              |")
        print("|To View Your Data Enter 2                      |")
        print("|To View Doctor's List Enter 3                  |")
        print("|To View All Hospital Depertment List Enter 4   |")
        print("|To be back enter 5                             |")
        print("-------------------------------------------------")
        usr_choice = int(input("Enter your choice : "))
        if usr_choice == 1 :
            self.usr_chk()
            i=self.idd
            for j in range(len(self.appointment_list)):
                if self.patient_list[i][0] == self.appointment_list[j][2] :
                    print("Appointment Id                   :",self.appointment_list[j][0])
                    print("Appointment Patient Name         :",self.appointment_list[j][1])
                    print("Appointment Patient Id           :",self.appointment_list[j][2])
                    print("Appointment Doctor Name          :",self.appointment_list[j][3])
                    print("Appointment Doctor Id            :",self.appointment_list[j][4])
                    print("Appointment Date                 :",self.appointment_list[j][5])
                    print("Appointment Session Start Time   :",self.appointment_list[j][6])
                    print("Appointment Session End Time     :",self.appointment_list[j][7])
            self.user()
        elif usr_choice == 2 :
            self.usr_chk()
            i=self.idd
            print("patient Id                    :",self.patient_list[i][0])
            print("patient Depertment            :",self.patient_list[i][1])
            print("patient name                  : ",self.patient_list[i][2])
            print("patient age                   : ",self.patient_list[i][3])
            print("patient gender                : ",self.patient_list[i][4])
            print("patient address               : ",self.patient_list[i][6])
            print("patient room number           : ",self.patient_list[i][5])
            print("patient is followed by doctor : ",self.patient_list[i][7])
            self.user()
        elif usr_choice == 3 :
            for i in range(len(self.doc)):
                print(f"Doctor {i+1} Name :",self.doc[i])
            self.user()
        elif usr_choice == 4 :
            for i in range(len(self.dept)):
                print(f"Dept {i+1} Name :",self.dept[i])
            self.user()
        elif usr_choice == 5 :
            self.menu()
        else:
            print("Enter Valid Choice!!")
            self.user()

c1=Hospital()


# In[ ]:




