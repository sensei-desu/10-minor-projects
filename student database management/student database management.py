class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_gpa(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0


def main():
    students = {}  # Stores student_id -> Student object

    while True:
        print("\n=== Student Record System ===")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Info")
        print("4. Quit")

        choice = input("Select an option (1-4): ").strip()

        if choice == '4':
            print("Bye!")
            break

        if choice == '1':
            name = input("Enter student name: ").strip()
            sid = input("Enter student ID: ").strip()
            if not name or not sid:
                print("Name and ID can't be empty.")
                continue
            if sid in students:
                print("A student with this ID already exists.")
            else:
                students[sid] = Student(name, sid)
                print(f"Added student: {name}")

        elif choice == '2':
            sid = input("Enter student ID: ").strip()
            if sid not in students:
                print("Student not found.")
                continue
            try:
                grade = float(input("Enter grade: "))
                students[sid].add_grade(grade)
                print("Grade recorded!")
            except ValueError:
                print("Please enter a valid number for the grade.")

        elif choice == '3':
            sid = input("Enter student ID: ").strip()
            if sid not in students:
                print("Student not found.")
                continue
            st = students[sid]
            print(f"\n--- {st.name} ({st.student_id}) ---")
            print(f"Grades : {st.grades if st.grades else 'None'}")
            print(f"GPA    : {st.calculate_gpa():.2f}")

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nScript crashed: {e}")
    finally:
        input("\nPress Enter to exit...")
