from database import get_connection


class EmployeeTaskManager:
    def __init__(self):

        self.connection = get_connection()
        self.cursor  =  self.connection.cursor()

    def add_employee(self):
        name= input("enter the employee name:")
        email=input("enter the email:")
        department=input("enter the department:")

        query = """
        INSERT INTO employees
        (name, email, department)
        VALUES (%s,%s,%s)
        """
        values = (name,email,department)
        self.cursor.execute(query,values)

        self.connection.commit()

        print("employee added successfully")

  

    def add_project(self):

        project_name=input("enter project name:")
        description=input("Enter the description")
        start_date=input("enter start date (YYYY-MM_DD): ")


        query="""
        INSERT INTO projects
        (project_name, description, start_date)
        VALUES(%s,%s,%s)
        """

        values=(project_name,description,start_date)
        self.cursor.execute(query,values)

        self.connection.commit()

        print("Project added successfully!")

    def assign_task(self):

        task_name=input("Enter task name: ")
        description=input("Enter task description: ")
        project_id=input("Enter project ID: ")
        employeee_id=input("Enter employee ID: ")
        priority =input("Enter priority(Low/Medium/High):")
        due_date= input("Enter due date(YYYY-MM-DD): ")

        query= """
        INSERT INTO tasks
        (task_name, description, project_id, employee_id, priority,due_date)
        """

        values =(
            task_name,
            description,
            project_id,
            employeee_id,
            priority,
            due_date
        )

        self.cursor.execute(query,values)

        self.connection.commit()

        print("Task assigned successfully !")


    def udpate_task_status(self):
        task_id=input("enter the task ID: ")
        new_status=input("Enter the status(pending/progress/completed): ")

        query="""
        UPDATE tasks
        SET status =%s
        WHERE task_id=%s
        """

        values=(new_status,task_id)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("TASK status update successfully")

    def search_tasks(self):
        status=input("Enter status to search (Pending/In progress/Completed): ")

        query="""
        SELECT
            t.task_id,
            t.task_name,
            t.description,
            t.project_id,
            t.employee_id,
            t.status,
            t.priority,
            t.due_date
        From tasks t

        JOIN projects p
            ON t.project_id = p.project_id

        JOIN employees e
            ON t.employee_id = e.employee_id
        WHERE status=%s
        """

        values=(status,)

        self.cursor.execute(query,values)

        tasks=self.cursor.fetchall()

        if len(tasks) ==0:
            print("No task found.")

        else:
            print("\n===========TASKA===========")

            for task in tasks:
                print("TASK ID:",task[0])
                print("TASK NAME:",task[1])
                print("Description:",task[2])
                print("Project ID:",task[3])
                print("Employee ID:",task[4])
                print("Status:",task[5])
                print("Priority:",task[6])
                print("Due Date:",task[7])
                print("----------------------------")


    def generate_reports(self):
        print("\n============Reports=============")
        print("\n1.Tasks by Employee")
        print("2. Task by Status")

        choice=input("enter the report choice")

        if choice =="1":
            query=""" 
            SELECT
                e.name,
                COUNT(t.task_id)
            FROM employees e
            LEFT JOIN tasks t
                ON e.employee_id =t.employee_id
            
            GROUP BY e.employee_id,e.name

            """

            self.cursor.execute(query)
            results = self.cursor.fetchall()

            print("\n-----------Tasks by Employee----------")

            for row in results:

                print("Employee:",row[0])
                print("Total Tasks: ",row[1])
                print("----------------------------------------")



        elif choice=="2":
            query="""

            SELECT
                status,
                COUNT(task_id)

            FROM tasks
            GROUP BY status
            """

            self.cursor.execute(query)
            results=self.cursor.fetchall()

            print("\n--------Task by Status----------")

            for row in results:

                print("Status:",row[0])
                print("Total Tasks:", row[1])
                print("-------------------------------")

        else:
            print("invalid report choice:")




    def run(self):
        while True:
            print("\n========================================")
            print(" Employee & Task Management System")
            print("========================================")  
            print("1. Add Employee")
            print("2. Add Project")
            print("3. Assign Task")
            print("4. Update Task Status")
            print("5. Search Tasks")
            print("6. Generate Reports")
            print("7. Exit") 
        
            choice=input("enter the choice:")
            if choice == "1":
                self.add_employee()
        
            elif choice == "2":
                self.add_project()
        
            elif choice == "3":
                self.assign_task()

        
            elif choice == "4":
                self.udpate_task_status()
        
            elif choice == "5":
                self.search_tasks()
        
            elif choice == "6":
                self.generate_reports()
        
            elif choice == "7":
                print("Thank you for using the system!")
                break


   
manager=EmployeeTaskManager()
manager.run()

