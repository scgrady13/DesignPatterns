class User:
    def __init__(self, user_data):
        self.user_data = user_data

    def get_role(self):
        raise NotImplementedError("Subclass must implement this method")


class Faculty(User):
    def get_role(self):
        return "Faculty"


class Student(User):
    def get_role(self):
        return "Student"


class Staff(User):
    def get_role(self):
        return "Staff"


class UserFactory:
    def create_user(self, user_data):
        if user_data["role"] == "Faculty":
            return Faculty(user_data)
        elif user_data["role"] == "Student":
            return Student(user_data)
        elif user_data["role"] == "Staff":
            return Staff(user_data)
        else:
            raise ValueError("Invalid role specified")


if __name__ == "__main__":
    user_factory = UserFactory()

    faculty_data = {"role": "Faculty", "name": "Dr. Smith"}
    faculty = user_factory.create_user(faculty_data)
    print(faculty.get_role())  # Output: Faculty

    student_data = {"role": "Student", "name": "Alice"}
    student = user_factory.create_user(student_data)
    print(student.get_role())  # Output: Student

    staff_data = {"role": "Staff", "name": "Bob"}
    staff = user_factory.create_user(staff_data)
    print(staff.get_role())  # Output: Staff

    # invalid_data = {"role": "Invalid", "name": "Invalid"}
    # invalid = user_factory.create_user(invalid_data)
    # print(invalid.get_role())  # Output: ValueError: Invalid role specified

