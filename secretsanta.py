import pandas as pd
import random

class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.secret_child = None

class SecretSanta:
    def __init__(self, employees, previous_assignments):
        self.employees = employees
        self.previous_assignments = previous_assignments

    def get_previous_assignments(self):
        try:
            assignments = {}
            for i, row in self.previous_assignments.iterrows():
                assignments[row['Employee_EmailID']] = row['Secret_Child_EmailID']
            return assignments
        except Exception as e:
            print(e)

    def assign_secret_santa(self):
        try:
            assignments = self.get_previous_assignments()
            available_children = [employee for employee in self.employees]

            for employee in self.employees:
                possible_children = [child for child in available_children if child.email != employee.email and assignments.get(employee.email) != child.email]
                if not possible_children:
                    raise ValueError("Cannot assign secret child without repeating last year's assignment")

                secret_child = random.choice(possible_children)
                employee.secret_child = secret_child
                available_children.remove(secret_child)
        except Exception as e:
            print(e)

    def get_results(self):
        try:
            results = []
            for employee in self.employees:
                results.append({
                    'Employee_Name': employee.name,
                    'Employee_EmailID': employee.email,
                    'Secret_Child_Name': employee.secret_child.name,
                    'Secret_Child_EmailID': employee.secret_child.email
                })
            return results
        except Exception as e:
            print(e)

    def save_results(self, output_file):
        try:
            results = self.get_results()
            df = pd.DataFrame(results)
            df.to_csv(output_file, index=False)
        except Exception as e:
            print(e)


def read_employees(file_path):
    try:
        df = pd.read_csv(file_path)
        employees = [Employee(row['Employee_Name'], row['Employee_EmailID']) for index, row in df.iterrows()]
        return employees
    except Exception as e:
        print(e)

def read_previous_assignments(file_path):
    return pd.read_csv(file_path)

def main():
    try:
        employees_file = 'employees.csv'
        previous_assignments_file = 'previous_assignments.csv'
        output_file = 'secret_santa_assignments.csv'

        employees = read_employees(employees_file)
        previous_assignments = read_previous_assignments(previous_assignments_file)

        secret_santa = SecretSanta(employees, previous_assignments)
        secret_santa.assign_secret_santa()
        secret_santa.save_results(output_file)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
