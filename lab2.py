from enum import Enum


class StudyField(Enum):
    MECHANICAL_ENGINEERING = "Mechanical Engineering"
    SOFTWARE_ENGINEERING = "Software Engineering"
    FOOD_TECHNOLOGY = "Food Technology"
    URBANISM_ARCHITECTURE = "Urbanism and Architecture"
    VETERINARY_MEDICINE = "Veterinary Medicine"


class Student:
    def __init__(self, first_name, last_name, email, enrolment_date, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrolment_date = enrolment_date
        self.date_of_birth = date_of_birth


class Faculty:
    def __init__(self, name, abbreviation, study_field):
        self.name = name
        self.abbreviation = abbreviation
        self.students = []
        self.graduates = []
        self.study_field = study_field

    def enroll_student(self, student):
        self.students.append(student)

    def graduate_student(self, student):
        if student in self.students:
            self.students.remove(student)
            self.graduates.append(student)

    def get_currently_enrolled_students(self):
        return [student for student in self.students]

    def get_graduates(self, ):
        return [graduate for graduate in self.graduates]


class University:
    def __init__(self):
        self.faculties = []

    def create_faculty(self, name, abbreviation, study_field):
        faculty = Faculty(name, abbreviation, study_field)
        self.faculties.append(faculty)
        return faculty

    def assign_student_to_faculty(self, student, faculty):
        faculty.enroll_student(student)
        print(f"Student {student.first_name} {student.last_name} assigned to {faculty.name}.")

    def graduate_student_from_faculty(self, student, faculty):
        faculty.graduate_student(student)
        print(f"Student {student.first_name} {student.last_name} graduated from {faculty.name}.")

    def display_currently_enrolled_students(self, faculty):
        print(f"Currently Enrolled Students in {faculty.name}:")
        students = faculty.get_currently_enrolled_students()
        for student in students:
            print(f"{student.first_name} {student.last_name}")

    def display_graduates(self,  faculty):
        print(f"Graduates from {faculty.name}:")
        graduates = faculty.get_graduates()
        for graduate in graduates:
            print(f"{graduate.first_name} {graduate.last_name}")

    def is_student_in_faculty(self, email, faculty):
        return any(student.email == email for student in faculty.students)

    def get_faculty_by_student_identifier(self, identifier):
        for faculty in self.faculties:
            for student in faculty.students:
                if student.email == identifier or student.unique_id == identifier:
                    return faculty
        return None

    def display_all_faculties(self):
        print("University Faculties:")
        for faculty in self.faculties:
            print(f"{faculty.name} ({faculty.abbreviation}) - {faculty.study_field.value}")

    def display_all_faculties_by_field(self, field):
        matching_faculties = [faculty for faculty in self.faculties if faculty.study_field == field]
        print(f"Faculties in {field.value}:")
        for faculty in matching_faculties:
            print(f"{faculty.name} ({faculty.abbreviation})")


# Interactive command line loop
def main():
    tum = University()

    while True:
        print("\nOptions:")
        print("1. Create a new faculty")
        print("2. Create and assign a student to a faculty")
        print("3. Graduate a student from a faculty")
        print("4. Display current enrolled students")
        print("5. Display graduates")
        print("6. Check if a student belongs to a faculty")
        print("7. Create a new student")
        print("8. Search what faculty a student belongs to by identifier")
        print("9. Display University faculties")
        print("10. Display all faculties belonging to a field")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter faculty name: ")
            abbreviation = input("Enter faculty abbreviation: ")
            field_input = input("Enter study field (e.g., MECHANICAL_ENGINEERING): ")
            study_field = StudyField[field_input]

            tum.create_faculty(name, abbreviation, study_field)
            print(f"Faculty {name} created.")

        elif choice == "2":
            email = input("Enter student email: ")
            faculty_name = input("Enter faculty name: ")

            faculty = next((f for f in tum.faculties if f.name == faculty_name), None)
            if faculty:
                first_name = input("Enter student first name: ")
                last_name = input("Enter student last name: ")
                enrolment_date = input("Enter enrolment date: ")
                date_of_birth = input("Enter date of birth: ")

                new_student = Student(first_name, last_name, email, enrolment_date, date_of_birth)
                tum.assign_student_to_faculty(new_student, faculty)

            else:
                print(f"No faculty found with the name {faculty_name}.")

        elif choice == "3":
            email = input("Enter student email to graduate: ")

            faculty = tum.get_faculty_by_student_identifier(email)
            if faculty:
                student_to_graduate = next((s for s in faculty.students if s.email == email), None)
                if student_to_graduate:
                    tum.graduate_student_from_faculty(student_to_graduate, faculty)
                else:
                    print(f"No student found with email {email} in {faculty.name}.")

            else:
                print(f"No faculty found for the student with email {email}.")

        elif choice == "4":
            faculty_name = input("Enter faculty name to display enrolled students: ")
            faculty = next((f for f in tum.faculties if f.name == faculty_name), None)
            if faculty:
                tum.display_currently_enrolled_students(faculty)
            else:
                print(f"No faculty found with the name {faculty_name}.")

        elif choice == "5":
            faculty_name = input("Enter faculty name to display graduates: ")
            faculty = next((f for f in tum.faculties if f.name == faculty_name), None)
            if faculty:
                tum.display_graduates(faculty)
            else:
                print(f"No faculty found with the name {faculty_name}.")


        elif choice == "6":
            email = input("Enter student email to check enrollment: ")
            faculty_name = input("Enter faculty name: ")
            faculty = next((f for f in tum.faculties if f.name == faculty_name), None)
            if faculty:
                if tum.is_student_in_faculty(email, faculty):
                    print(f"Yes, the student with email {email} belongs to {faculty.name} faculty.")
                else:
                    print(f"No, the student with email {email} does not belong to {faculty.name} faculty.")
            else:
                print(f"No faculty found with the name {faculty_name}.")

        elif choice == "7":
            first_name = input("Enter student first name: ")
            last_name = input("Enter student last name: ")
            email = input("Enter student email: ")
            enrolment_date = input("Enter enrolment date: ")
            date_of_birth = input("Enter date of birth: ")

            new_student = Student(first_name, last_name, email, enrolment_date, date_of_birth)
            print(f"Student {new_student.first_name} {new_student.last_name} created.")

        elif choice == "8":
            identifier = input("Enter student email or unique ID: ")
            faculty = tum.get_faculty_by_student_identifier(identifier)
            if faculty:
                print(f"The student with identifier {identifier} belongs to {faculty.name} faculty.")
            else:
                print(f"No faculty found for the student with identifier {identifier}.")

        elif choice == "9":
            tum.display_all_faculties()

        elif choice == "10":
            field_input = input("Enter study field (e.g., MECHANICAL_ENGINEERING): ")
            study_field = StudyField[field_input]
            tum.display_all_faculties_by_field(study_field)

        elif choice == "11":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
