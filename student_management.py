import json
import os

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "grades": self.grades
        }

class Classroom:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_from_file()

    def add_student(self, name, sid):
        if any(s.student_id == sid for s in self.students):
            return False, f"Error: Student ID {sid} already exists. Please enter a unique ID."
        
        new_student = Student(name, sid)
        self.students.append(new_student)
        return True, f"Added {name}!"

    def find_student_by_id(self, sid):
        for student in self.students:
            if student.student_id == sid:
                return student
        return None

    def remove_student(self, student):
        self.students.remove(student)

    def search_students(self, query):
        query = query.lower()
        results = []
        for student in self.students:
            if query in student.name.lower() or query in student.student_id:
                results.append(student)
        return results

    def save_to_file(self):
        try:
            with open(self.filename, "w") as file:
                all_data = [student.to_dict() for student in self.students]
                json.dump(all_data, file, indent=4)
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_from_file(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    if isinstance(data, list):
                        for s_data in data:
                            student = Student(s_data["name"], s_data["student_id"])
                            student.grades = s_data["grades"]
                            self.students.append(student)
            except (json.JSONDecodeError, KeyError):
                print("Note: Could not load previous data due to file corruption. Starting fresh!")

def main():
    classroom = Classroom()

    while True:
        print("\n--- Student Management Menu ---")
        print("1. Add a Student")
        print("2. List Students")
        print("3. Add Grade")
        print("4. Search Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")

        if choice == "1":
            name = input("Enter Student Name: ")
            sid = input("Enter Student ID: ")
            success, message = classroom.add_student(name, sid)
            print(message)

        elif choice == "2":
            if not classroom.students:
                print("The classroom is empty.")
            else:
                print("\n" + "="*45)
                print(f"{'#':<3} | {'Name':<20} | {'ID': <8} | {'Avg':<6}")
                print("-" * 45)
                for index, student in enumerate(classroom.students):
                    print(f"{index + 1:<3} | {student.name:<20} | {student.student_id:<8} | {student.get_average():<6.2f}")
                print("-" * 45)

        elif choice == "3":
            if not classroom.students:
                print("The classroom is empty.")
            else:
                sid = input("Enter Student ID: ")
                student = classroom.find_student_by_id(sid)
                
                if student:
                    try:
                        grade = int(input(f"Enter Grade for {student.name}: "))
                        student.add_grade(grade)
                        print(f"Added grade {grade} for {student.name}")
                    except ValueError:
                        print("Invalid grade. Please enter a valid integer.")
                else:
                    print(f"Student with ID '{sid}' not found.")
                
        elif choice == "4":
            query = input("Enter Name or ID of the student: ").lower()
            results = classroom.search_students(query)

            if not results:
                print(f"No results found matching '{query}'.")
            else:
                print(f"\nFound {len(results)} results: ")
                print(f"{'Name':<20} | {'ID':<8} | {'Avg':<6}")
                print("-" * 37)
                for student in results:
                    print(f"{student.name:<20} | {student.student_id:<8} | {student.get_average():<6.2f}")
                print("-" * 37)
                
        elif choice == "5":
            if not classroom.students:
                print("The classroom is empty.")
            else:
                sid = input("Enter Student ID to delete: ")
                student = classroom.find_student_by_id(sid)

                if student:
                    confirm = input(f"Are you sure you want to delete {student.name}? (y/n): ").lower()
                    if confirm == 'y':
                        classroom.remove_student(student)
                        print(f"Deleted {student.name} from the classroom successfully.")
                    else:
                        print("Operation cancelled.")
                else:
                    print(f"Student with ID '{sid}' not found.")
                
        elif choice == "6":
            classroom.save_to_file()
            print("Thank you for using the Student Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
