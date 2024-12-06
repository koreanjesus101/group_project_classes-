class Doctor:
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
 
    # Getter methods
    def get_doctor_id(self):
        return self.doctor_id
 
    def get_name(self):
        return self.name
 
    def get_specialization(self):
        return self.specialization
 
    def get_working_time(self):
        return self.working_time
 
    def get_qualification(self):
        return self.qualification
 
    def get_room_number(self):
        return self.room_number
 
    # Setter methods
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id
 
    def set_name(self, new_name):
        self.name = new_name
 
    def set_specialization(self, new_specialization):
        self.specialization = new_specialization
 
    def set_working_time(self, new_working_time):
        self.working_time = new_working_time
 
    def set_qualification(self, new_qualification):
        self.qualification = new_qualification
 
    def set_room_number(self, new_room_number):
        self.room_number = new_room_number
 
    # String representation of the Doctor object
    def __str__(self):
        return (f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}, "
                f"Working Time: {self.working_time}, Qualification: {self.qualification},"
                f" Room Number: {self.room_number}")
 
 
class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()
 
    @staticmethod
    def format_dr_info(doctor):
        return f"{doctor.doctor_id}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_number}"
 
    @staticmethod
    def enter_dr_info():
        doctor_id = input("Enter doctor ID: ")
        name = input("Enter doctor name: ")
        speciality = input("Enter doctor speciality: ")
        timing = input("Enter doctor timing: ")
        qualification = input("Enter doctor qualification: ")
        room_number = input("Enter doctor room number: ")
        return Doctor(doctor_id, name, speciality, timing, qualification, room_number)
 
    def read_doctors_file(self):
        try:
            with open("doctors.txt", "r") as file:
                for line in file.readlines()[1:]:  # Skip header
                    data = line.strip().split("_")
                    if len(data) == 6:  # Ensure the line has all required fields
                        doctor = Doctor(*data)
                        self.doctors.append(doctor)
                    else:
                        print(f"Skipping malformed line: {line.strip()}")
        except FileNotFoundError:
            print("Error: doctors.txt not found. Starting with an empty list.")
 
    def search_doctor_by_id(self):
        doctor_id = input("Enter the doctor's ID: ") .strip()
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                print("\nID       Name                 Specialization       Timing          Qualification       Room Number")
                print(f"{doctor.doctor_id:<8} {doctor.name:<20} {doctor.specialization:<20} {doctor.working_time:<15} {doctor.qualification:<15} {doctor.room_number}")
                return
        print("\nCan’t find the doctor with the same ID in the system.")
 
    def search_doctor_by_name(self):
        doctor_name = input("Enter doctor name: ").strip().lower().replace(" ", "")
        for doctor in self.doctors:
            if doctor.get_name().lower().replace(" ", "")== doctor_name: 
                print("\nID       Name                 Specialization       Timing          Qualification       Room Number")
                print(f"{doctor.doctor_id:<8} {doctor.name:<20} {doctor.specialization:<20} {doctor.working_time:<15} {doctor.qualification:<15} {doctor.room_number}")
                return
        print("\nCan’t find the doctor with the same name in the system.")
 

    def edit_doctor_info(self):
        doctor_id = input("Please Enter the ID of the doctor that you want to edit:")
        for doctor in self.doctors:
             if doctor.get_doctor_id() == doctor_id:
                doctor.set_name(input(f"Enter new name (current: {doctor.get_name()}): "))
                doctor.set_specialization(input(f"Enter new specialization (current: {doctor.get_specialization()}): "))
                doctor.set_working_time(input(f"Enter new working time (current: {doctor.get_working_time()}): "))
                doctor.set_qualification(input(f"Enter new qualification (current: {doctor.get_qualification()}): "))
                doctor.set_room_number(input(f"Enter new room number (current: {doctor.get_room_number()}): "))
                self.write_list_of_doctors_to_file()
                print("\nDoctor info updated.")
                return
        print("\nCannot find the doctor...")
 
    def display_doctors_list(self):
        print("\nID       Name                 Specialization       Timing          Qualification       Room Number")
        for doctor in self.doctors:
            print(f"{doctor.doctor_id:<8} {doctor.name:<20} {doctor.specialization:<20} {doctor.working_time:<15} {doctor.qualification:<15} {doctor.room_number}")

    def write_list_of_doctors_to_file(self):
        with open("doctors.txt", "w") as file:
            file.write("id_name_specialist_timing_qualification_roomNb\n")  # Write header
            for doctor in self.doctors:
                file.write(self.format_dr_info(doctor) + "\n")
 
    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        with open("doctors.txt", "a") as file:
                file.write(self.format_dr_info(new_doctor) + "\n")
                print("New doctor added.")
 
 
# class 4
class Patient:
    def __init__(self, patients_id="", name="", disease="", gender="", age=""):
        self.patients_id = patients_id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age
 
    def __str__(self):
        return f"{self.patients_id}{self.name}{self.disease}{self.gender}{self.age}"
 
 
class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()
 
    @staticmethod
    def format_patient_info_for_file(patient):
        return str(patient)
 
    @staticmethod
    def enter_patient_info():
        new_patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")
        return Patient(new_patient_id, name, disease, gender, age)
 
    def read_patients_file(self):
        with open("patients.txt", "r") as file:
            for line in file:
                patient_data = line.strip().split("_")
                self.patients.append(patient_data)
 
    def search_patient_by_id(self):
        patients_id = input("Enter patient ID: ")
        for patient in self.patients:
            if patient[0] == patients_id:
                print(f"{'ID':<10}{'Name':<20}{'Disease':<20}{'Gender':<20}{'Age':<20}")
                print(f"{patient[0]:>0} {patient[1]:>11} {patient[2]:>23} {patient[3]:>16}{patient[4]:>18}")
                return
        print("Can’t find the patient…")
 
    @staticmethod
    def display_patient_info(patient):
        print(f"{patient[0]:>0} {patient[1]:>11} {patient[2]:>23} {patient[3]:>16}{patient[4]:>18}")
 
    def edit_patient_info_by_id(self):
        patients_id = input("Enter patient ID to edit: ")
        for patient in self.patients:
            if patient[0] == patients_id:
                patient[1] = input("Enter new name: ")
                patient[2] = input("Enter new disease: ")
                patient[3] = input("Enter new gender: ")
                patient[4] = input("Enter new age: ")
                self.write_list_of_patients_to_file()
                print("Patient info updated.")
                return
        print("Cannot find the patient…")
 
    def display_patients_list(self):
        for patient in self.patients:
            self.display_patient_info(patient)
 
    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient) + "\n")
 
    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        with open("patients.txt", "a") as file:
            file.write(self.format_patient_info_for_file(new_patient) + "\n")
        print(f"New patient is added.")
 
 
class Management:
    def __init__(self):
        self.doctor_manager = doctor_manager
        self.patient_manager = patient_manager
 
    def display_menu(self):
        while True:
            print("\nWelcome to Alberta Hospital (AH) Management system")
            print("Select from the following options, or select 0 to stop:")
            print("1 - Doctors")
            print("2 - Patients")
            print("3 - Exit Program")
 
            choice = input(">>> ")
 
            if choice == "1":
                self.display_doctors_menu()
            elif choice == "2":
                self.display_patients_menu()
            elif choice == "3":
                print("Thanks for using the program. Bye!")
                break
            else:
                print("Invalid choice. Please try again.")
 
    def display_doctors_menu(self):
        while True:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add New doctor")
            print("5 - Edit doctor information")
            print("6 - Back to the Main Menu")
 
            choice = input(">>> ")
 
            if choice == "1":
                self.doctor_manager.display_doctors_list()
            elif choice == "2":
                self.doctor_manager.search_doctor_by_id()
            elif choice == "3":
                self.doctor_manager.search_doctor_by_name()
            elif choice == "4":
                self.doctor_manager.add_dr_to_file()
            elif choice == "5":
                self.doctor_manager.edit_doctor_info()
            elif choice == "6":
                print("Returning to the main menu...")
                break
            else:
                print("Invalid choice. Please try again.")
 
    def display_patients_menu(self):
        while True:
            print("\nPatients Submenu:")
            print("1 - Display Patient List")
            print("2 - Search Patient by ID")
            print("3 - Add New Patient")
            print("4 - Edit Patient information")
            print("5 - Back to the Main Menu")
 
            choice = input(">>> ")
 
            if choice == "1":
                self.patient_manager.display_patients_list()
            elif choice == "2":
                self.patient_manager.search_patient_by_id()
            elif choice == "3":
                self.patient_manager.add_patient_to_file()
            elif choice == "4":
                self.patient_manager.edit_patient_info_by_id()
            elif choice == "5":
                print("Returning to the main menu...")
                break
            else:
                print("Invalid choice. Please try again.")
 
 
doctor_manager = DoctorManager()
patient_manager = PatientManager()
management = Management()
management.display_menu()