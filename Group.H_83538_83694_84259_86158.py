'''
Class Admin, Class Housing College administrator 
Implemented by Kong Wang Seng (84259)

Class Maintenance Team, Class Fault Tracking System 
Implemented by Katherine Wong Sing Hie (86158)

Class Student, Class Emergemcy report 
Implemented by Clarence Chin Wei Yong (83538)

Class Inventory 
Implemented by Eddy Lau Bi Piau (83694)
'''

import time
import random

class Admin:
    def __init__(self, admin_id, admin_name, staff_id, administrator_id, password):
        self.AdminID = admin_id
        self.AdminName = admin_name
        self.StaffID = staff_id
        self.AdministratorID = administrator_id
        self.password = password
        self.feedback_collection = []  # List to store feedback
        
    def Login(self):
        entered_admin_id = input("Enter AdminID: ")
        entered_password = input("Enter password: ")

        if entered_admin_id == str(self.AdminID) and entered_password == self.password:
            print("Login successful!")
            return True
        else:
            print("Login failed. Incorrect AdminID or password.")
            return False
        
    def CollectFeedback(self, student, service_quality_feedback, satisfaction_rating):
        feedback_entry = {
            "StudentName": student.get_student_name(),
            "ServiceQualityFeedback": service_quality_feedback,
            "SatisfactionRating": satisfaction_rating
        }
        self.feedback_collection.append(feedback_entry)
        print(f"Feedback collected from {student.get_student_name()}.")

    
    def ViewAllFeedback(self):
        if not self.feedback_collection:
            print("No feedback in the list!")
        else:
            print("All submitted feedback:")
            for feedback_entry in self.feedback_collection:
                print(f"Student: {feedback_entry['StudentName']}")
                print(f"Service Quality Feedback: {feedback_entry['ServiceQualityFeedback']}")
                print(f"Satisfaction Rating: {feedback_entry['SatisfactionRating']}")
                print("-----------------------------")


    def CollectFeedbackMenu(self, students):
        print("\nCollect Feedback Menu:")
        student_id = input("Enter student ID to collect feedback: ")
        found_student = next((student for student in students if student.get_student_id() == student_id), None)

        if found_student:
            service_quality_feedback = input("Enter feedback for service quality: ")
            satisfaction_rating = input("Enter satisfaction rating (1-5): ")

            if satisfaction_rating.isdigit() and 1 <= int(satisfaction_rating) <= 5:
                self.CollectFeedback(found_student, service_quality_feedback, int(satisfaction_rating))
            else:
                print("Invalid satisfaction rating. Feedback collection aborted.")
        else:
            print(f"Student with ID {student_id} not found. Feedback collection aborted.")
            
class HousingCollegeAdministrator(Admin):
    assigned_issues = []
    def __init__(self, admin_id, admin_name, staff_id, administrator_id, password):
        super().__init__(admin_id, admin_name, staff_id, administrator_id, password)
        self.AdministratorName = admin_name  # Additional attribute for HousingCollegeAdministrator
        self.assigned_team = None
        HousingCollegeAdministrator.assigned_issues.append(self)
    
    def ScheduleMaintenance(self, student, issue_description):
        maintenance_entry = {
            "StudentName": student.get_student_name(),
            "IssueDescription": issue_description
        }

        # Assume there is a list to store scheduled maintenance
        scheduled_maintenance_list = []  # You can initialize this list in the __init__ method if needed
        scheduled_maintenance_list.append(maintenance_entry)

        print(f"Maintenance scheduled successfully for {student.get_student_name()}.")
        print(f"Issue Description: {issue_description}")
       
    def assign_issue_to_team(self, emergency_report, maintenance_team):
        maintenance_team.assignIssue(emergency_report)

    def assign_issue_menu(self, emergency_reports, maintenance_teams):
        print("\nAssign Issue to Maintenance Team Menu:")
        
        # Display available emergency reports
        print("Available Emergency Reports:")
        for i, report in enumerate(emergency_reports, start=1):
            print(f"{i}. Emergency Report ID: {report.reportID}\nRoom ID: {report.roomID}\nDescription: {report.description}\n")
        
        # User selects an emergency report
        report_choice = input("Select an emergency report to assign (1-{}): ".format(len(emergency_reports)))
        selected_report_index = int(report_choice) - 1

        if 0 <= selected_report_index < len(emergency_reports):
            selected_report = emergency_reports[selected_report_index]
                
            print("\nAvailable Maintenance Teams:")
            available_teams = [team for team in maintenanceTeam.registered_teams if team.staff_status == "A"]

            if not available_teams:
                print("No available maintenance teams.")
            else:
                for i, team in enumerate(available_teams, start=1):
                    print(f"{i}. Staff {team.staff_name} ({team.staff_status})")

                team_choice = input("Select an available maintenance team (1-{}): ".format(len(available_teams)))
                selected_team_index = int(team_choice) - 1

                if 0 <= selected_team_index < len(available_teams):
                    selected_team = available_teams[selected_team_index]
                
                # Assign the issue to the selected maintenance team
                    self.assign_issue_to_team(selected_report, selected_team)
                    print(f"Emergency Report ID {selected_report.reportID} assigned to Maintenance Team {selected_team.staff_name}.")
                else:
                    print("Invalid team selection, please input a valid ID")

        else:
            print("Invalid report selection.")
        
    def LogIn(self):
        entered_administrator_id = input("Enter AdministratorID: ")
        entered_password = input("Enter password: ")

        if entered_administrator_id == str(self.AdministratorID) and entered_password == self.password:
            print("Login successful!")
            return True
        else:
            print("Login failed. Incorrect AdministratorID or password.")
            return False

class maintenanceTeam():
    registered_teams = []
    def __init__(self, staff_id, staff_name, staff_status, staff_email, contact_no, staff_password):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.staff_status = staff_status
        self.staff_email = staff_email
        self.contact_no = contact_no
        self.staff_password = staff_password
        maintenanceTeam.registered_teams.append(self)
        self.assigned_issue = []
        self.inventory = []
       
    @classmethod
    def registerNewTeam(cls):
        print("\n--- Registration ---")
        print("Please fill in the details.")
        staff_id = input("Staff ID: ")
        staff_name = input("Staff Name: ")
        staff_status = input("Staff Status (A = Available, NA = Not Available): ").capitalize()
        staff_email = input("Staff Email: ")
        contact_no = input("Contact Number: ")
        staff_password = input("Password: ")

        # Check if ID is already taken
        if any(team.staff_id == staff_id for team in cls.registered_teams):
            print(f"Staff {staff_id} is already registered.")
            return None

        # Create a new instance of the maintenanceTeam class
        new_team = cls(staff_id, staff_name, staff_status, staff_email, contact_no, staff_password)
        print(f"{staff_name} registered successfully!")
        return new_team
    
    def updateTeamStatus(self, new_status):
        self.staff_status = new_status
        print(f"\nStatus updated to {new_status}")
        print(f"Staff ID: {login_team.staff_id}\nStaff Name: {login_team.staff_name}\nStaff Status: {login_team.staff_status}\n")
    
    def assignIssue(self, issue):
        if issue not in self.assigned_issue:
            self.assigned_issue.append(issue)
            issue.assigned_team = self        
           
    def view_assignedIssues(self):
        sorted_issues = sorted(self.assigned_issue, key=lambda x: x.get_report_id())
        print(f"\n---Assigned Issues for {self.staff_name}---")
        for issue in sorted_issues:
            print(f"Student ID: {issue.get_student_id()}\nIssue ID: {issue.get_report_id()}\nRoom Number: {issue.get_room_id()}\nDescription: {issue.get_description()}\nDate and Time: {time.ctime(issue.get_date_time())}\nStatus: {issue.get_status()}\n")
            
    def updateIssueStatus(self):
        print("\n---Update Issue Status---")

        while True:
            issueID = input("\nEnter the issue ID you want to update: ")

        # Check if the issue ID is a numeric value
            if not issueID.isdigit():
                print("Please enter a valid issue ID.")
                continue
            
            issueID = int(issueID)

        # Check if the ID is in assigned issues list
            matching_issues = [issue for issue in self.assigned_issue if issue.get_report_id() == issueID]

            if not matching_issues:
                print(f"Issue ID {issueID} is not found in the assigned issues.")
                break
            
            valid_statuses = ["Pending", "Settled"]
            new_issueStatus = input(f"Enter the new status ({', '.join(valid_statuses)}): ").capitalize()

            if new_issueStatus not in valid_statuses:
                print("Invalid status! Please enter a valid status.")
                continue
             
            for issue in matching_issues:
                issue.update_status(new_issueStatus)
                print(f"Status of Issue ID {issueID} updated to {new_issueStatus}")
                return
  
    def checkInventory(self):
        print("\n---Inventory List---")
        for item in InventoryItem.itemList:
            print(f"Item ID: {item.itemID}\nItem Name: {item.itemName}\n"
                  f"Item Quantity: {item.itemQuantity}\n"
                  f"Item Category: {item.itemCategory}\n") 
            
    def updateInventory(self):
        print("\n---Update Inventory Quantity---")
        
        while True:
            itemID = input("Enter the item ID you want to update: ")
            
            if not itemID.isdigit():
                print("Please enter a valid item ID.")
                continue
            
            if not any (item.itemID == itemID for item in InventoryItem.itemList):
                print("Item is not found.")
                break
            
            newQuantity = input("Enter the new quantity: ")
        
            if not newQuantity.isdigit():
                print("Please enter a valid numeric quantity.")
                continue
            
            for item in InventoryItem.itemList:
                if item.itemID == itemID:
                    item.itemQuantity = newQuantity
                    print(f"\nItem Name: {item.itemName}\n"
                          f"Item Quantity: {item.itemQuantity}\n"
                          f"Item Category: {item.itemCategory}\n") 
                    return
                
    def TeamAvailability(self):  
        print ("\nA = Available, NA = Not Available") 
        print (f"Current log in as Staff: {self.staff_name}\nStaff Status: {self.staff_status}")

class FaultTrackSystem:
    @staticmethod
    def generate_report(maintenance_team):
        print("\n---Maintenance Team Performance Report---")

        for team in maintenance_team:
            print(f"\nStaff ID: {team.staff_id}\nStaff Name: {team.staff_name}")

            # Initialize status counts
            status_counts = {"Pending": 0, "Settled": 0}

            for issue in team.assigned_issue:
                # Print the actual status to understand the issue
                print(f"Issue ID: {issue.get_report_id()}, Actual Status: {issue.get_status()}")

                # Increment the count based on the actual status
                if issue.get_status() in status_counts:
                    status_counts[issue.get_status()] += 1

            print(f"Total pending issues: {status_counts['Pending']}")
            print(f"Total settled Issues: {status_counts['Settled']}")

            if status_counts['Pending'] + status_counts['Settled'] > 0:
                completion_percentage = (status_counts['Settled'] / (status_counts['Pending'] + status_counts['Settled'])) * 100
                print(f"Completion Percentage: {completion_percentage:.2f}%")
            else:
                print("No assigned issues.")   

class InventoryItem:
    itemList = []
    def __init__(self, itemID, itemName, itemQuantity, itemCategory):
        self.itemID = itemID
        self.itemName = itemName
        self.itemQuantity = itemQuantity
        self.itemCategory = itemCategory
        InventoryItem.itemList.append(self)
        
class Inventory:
    def __init__(self, TeamID, missing_part, new_material):
        self.TeamID = TeamID 
        self.MissingPart = missing_part
        self.Material = new_material
        self.Quantity = 0  # Assuming Quantity should be an attribute
        self.PartOrder = ""        

    def OrderMissingPart(self, new_order_quantity):
        self.Quantity += new_order_quantity
        self.PartOrder = self.MissingPart

    def UpdatePart(self, new_material, new_quantity):
        self.Material = new_material
        self.Quantity = int(new_quantity)  # Convert to integer

    def CalculateInventoryPrice(self, roomID):
        self.RoomID = roomID 
        random_float = round(random.uniform(0.00, 250.00), 2)
        print(f"This is the inventory price for Room ID '{self.RoomID}' RM: {random_float}")
        
class Student:
    def __init__(self, id, name, email, contact_number, pwd):
        self.studentID = id
        self.studentName = name
        self.studentEmail = email
        self.studentContactNumber = contact_number
        self.password = pwd
        self.feedback_collection = []

    def get_student_id(self):
        return self.studentID

    def get_student_name(self):
        return self.studentName

    def get_student_email(self):    
        return self.studentEmail

    def get_student_contact_number(self):
        return self.studentContactNumber

    def get_password(self):
        return self.password

    def register_account(self):
        print("Please fill in the details:")
        self.studentName = input("Enter name: ")
        self.studentEmail = input("Enter email: ")
        self.studentContactNumber = int(input("Enter contact number: "))
        self.password = input("Enter password (alphanumeric): ")
        print(f"The account has successfully been registered for the student: {self.studentName}")

    def update_information(self):
        print("Update student information:")
        student_id_input = input("Enter your student ID: ")
        password_input = input("Enter your password: ")

        if student_id_input == self.studentID and password_input == self.password:
            self.studentContactNumber = int(input(f"You have success login to your account! \n\nEnter new contact number for student {self.studentID}: "))
            self.password = input("Enter new password for student (alphanumeric): ")
            print(f"Information updated for student {self.studentID} \nThe account has been logged out")
        else:
            print("Invalid student ID or password. Information not updated.")

    def report_issue(self):
        print("you have success login to your account! \nyou may report the issue")
        issue_description = input("Enter issue description: ")
        issue_id = len(emergency_reports) + 1
        issue_status = "Pending"

        emergency_report = EmergencyReport(issue_id, "", issue_description, self.studentID, time.time(), issue_status)
        emergency_reports.append(emergency_report)

        print(f"Issue reported successfully. Issue ID: {issue_id} \nThe account has been logged out!")
        
    def CollectFeedback(self, service_quality_feedback, satisfaction_rating):
         feedback_entry = {
             "StudentName": self.get_student_name(),
             "ServiceQualityFeedback": service_quality_feedback,
             "SatisfactionRating": satisfaction_rating
         }
         self.feedback_collection.append(feedback_entry)
         print(f"Feedback collected from {self.get_student_name()}.")

class EmergencyReport:
    def __init__(self, id, room, desc, student_id, dt, stat):
        self.reportID = id
        self.roomID = room
        self.description = desc
        self.studentID = student_id
        self.dateTime = dt
        self.status = stat

    def get_report_id(self):
        return self.reportID

    def get_room_id(self):
        return self.roomID

    def get_description(self):
        return self.description

    def get_student_id(self):
        return self.studentID

    def get_date_time(self):
        return self.dateTime

    def get_status(self):
        return self.status

    def update_status(self, new_issueStatus):
        print(f"Choose status for report ID {self.reportID}:")
        print("1. Pending")
        print("2. Settled")
        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            self.status = "Pending"
        elif choice == "2":
            self.status = "Settled"
        else:
            print("Invalid choice. Status remains unchanged.")

        print(f"Status updated for report ID {self.reportID}")

    def display_emergency_report(self):
        print("-------------------------------------")
        print(f"Emergency Report ID: {self.reportID}")
        print(f"Room ID: {self.roomID}")
        print(f"Description: {self.description}")
        print(f"Student ID: {self.studentID}")
        print(f"Date and Time: {time.ctime(self.dateTime)}")
        print(f"Status: {self.status}")
        print("-------------------------------------\n")

    def make_report(self):
        print("you have success login to your account! \n\nMake an emergency report:")
        self.roomID = input("Enter room ID: ")
        self.description = input("Enter issue description: ")
        self.status = "Pending"
        print("Emergency report created.")

def student_menu():
    print("\nStudent Menu:")
    print("1. Register account")
    print("2. Make an emergency report")
    print("3. Update student information")
    print("4. Report Issue")
    print("5. Provide Feedback")
    print("6. Exit")
    
def registrationStaff():
        new_team = maintenanceTeam.registerNewTeam()
        if new_team:
            maintenanceTeam.registered_teams.append(new_team)
            print("Registration successful.")
            return new_team

def loginStaff():
    global login_team  # Declare login_team as a global variable

    while True:
        print("\nLogin Maintenance Team")
        staff_id = input("Staff ID: ")
        if not staff_id.isdigit():
            print("Please enter a valid team ID.\n")
            continue
        
        if staff_id not in [team.staff_id for team in maintenanceTeam.registered_teams]:
            print(f"{staff_id} is not registered. Please enter a valid Team ID.\n")
            continue
        
        staff_password = input("Password: ")

        for team in maintenanceTeam.registered_teams:
            if team.staff_id == staff_id and team.staff_password == staff_password:
                print("Login successful.\n")
                login_team = team  # Assign the team to the global variable login_team
                return login_team

        print("Login failed. Please try again. \n")

def maintenanceTeamMainPage():
    while True:
        print("\nMaintenance Team Main Page")
        print("1. Register")
        print("2. Log in")
        print("3. Exit")
        
        t_choice = input("Enter your choice: ")
        
        if t_choice == "1":
            login_team = registrationStaff()
            if login_team:
                continue
        elif t_choice == "2":
                login_team = loginStaff()
                if login_team:
                    while True:
                        print("\nMaintenance Team Menu")
                        print("1. Check Inventory")
                        print("2. Update Inventory")
                        print("3. View Assigned Issues")
                        print("4. Update Issues Status")
                        print("5. Update Team Status")
                        print("6. Order Missing Part.")
                        print("7. Check for update part is in stock.")
                        print("8. Calculate inventory price.")
                        print("9. Check the avaibility of the Team.")
                        print("10. View Report")
                        print("11. Exit")
                        
                        staff_choice = input("Enter your choice: ")
                        
                        if staff_choice == "1":
                            login_team.checkInventory()
                            
                        elif staff_choice == "2":
                            login_team.updateInventory()
        
                        elif staff_choice == "3":
                            login_team.view_assignedIssues()
        
                        elif staff_choice == "4":
                            login_team.view_assignedIssues()
                            login_team.updateIssueStatus()
    
                        elif staff_choice == "5":
                            print("\n---Changing Team Status---")
                            print(f"Staff ID: {login_team.staff_id}\nStaff Name: {login_team.staff_name}\nStaff Status: {login_team.staff_status}\n(A = Available, NA = Not Available)")
                            new_status = input("Enter new status [A or NA]: ").capitalize()
                            login_team.updateTeamStatus(new_status)
                            
                        
                        elif staff_choice == "6":
                            missing_part = input("What missing part would you like to order: ")
                            new_order_quantity = int(input("Enter the quantity to order: "))
                            if new_order_quantity > 0:
                                inventory_instance.OrderMissingPart(new_order_quantity)
                                print(f"---Order placed for {new_order_quantity} {missing_part}---")
                            else:
                                print("Invalid quantity.")
                        elif staff_choice == "7":
                            for new_material, new_quantity in preset_updates:
                                if new_quantity > 1:
                                    print("-------------------------------------------------")
                                    print("---Your ordered part is back in stock!---")
                                    
                                else:
                                    print("-------------------------------------------------")
                                    print("---Your ordered part is not yet back in stock!---")
                                   
                                inventory_instance.UpdatePart(new_material, new_quantity)
                                print(f"---Available of {new_quantity} {new_material}---") 
                            
                        elif staff_choice == "8":
                            roomID = int(input("Please enter the Room ID:"))
                            inventory_instance.CalculateInventoryPrice(roomID)
                            
                        elif staff_choice == "9":
                            login_team.TeamAvailability()

                        elif staff_choice == "10":   
                            FaultTrack.generate_report(maintenanceTeam.registered_teams)
                            
                        elif staff_choice == "11":
                            print("\nYou have exited maintenance page.")
                            return maintenanceTeamMainPage()
    
                        else:
                            print("Invalid option! Please try again!\n")
                    break
                
        elif t_choice == '3': 
            print("Exit")
            return
            
        else:
            print("Invalid")

# Main program
students = []
emergency_reports = []
admin_instance = Admin(admin_id=1, admin_name="Samuel", staff_id=100, administrator_id="admin123", password="Password123")
housing_admin_instance = HousingCollegeAdministrator(admin_id=2, admin_name="Jack", staff_id=102, administrator_id= 200,password="Password123")
team1 = maintenanceTeam("1", "A", "A", "teamA@gmail.com", "03-11110", "teamA1234")
team2 = maintenanceTeam("2", "B", "A", "teamB@gmail.com", "03-11111", "teamB1234")
team3 = maintenanceTeam("3", "C", "NA", "teamC@gmail.com", "03-11112", "teamC1234")
team4 = maintenanceTeam("4", "D", "NA", "teamD@gmail.com", "03-11113", "teamD1234")
team5 = maintenanceTeam("5", "E", "A", "teamE@gmail.com", "03-11114", "teamE1234")
maintenance_teams = maintenanceTeam.registered_teams
FaultTrack = FaultTrackSystem()
item1 = InventoryItem("1", "Screws", 100, "Hardware")
item2 = InventoryItem("2", "Wrenches", 50, "Tools")
item3 = InventoryItem("3", "Bulbs", 200, "Electrical")
item4 = InventoryItem("4", "Batteries", 30, "Electrical")
item5 = InventoryItem("5", "Cleaning Supplies", 15, "Cleaning")

#preset data for Inventory
inventory_instance = Inventory("TeamA", "", "")
preset_updates = [("screw", 4), ("bolt", 0), ("bulb", 3), ("nut", 1), ("rivet", 2)]

while True:
    print("\nWelcome to the Residential College Fault Tracking System!")
    print("Choose user type:")
    print("1. Student")
    print("2. Admin")
    print("3. Housing College Administrator")
    print("4. Maintenance Team")
    print("5. Exit")
    user_choice = input("Enter your choice (1-5): ")

    if user_choice == "1":
        # Student menu
        while True:
            student_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                # Register account
                student_id = input("Enter student ID: ")

                student = Student(student_id, "", "", 0, "")
                student.register_account()
                students.append(student)

            elif choice == "2":
                # Make an emergency report
                student_id = input("Enter student ID: ")
                password = input("Enter password: ")
                found_student = next((student for student in students if student.get_student_id() == student_id and student.get_password() == password), None)

                if found_student:
                    emergency_report = EmergencyReport(len(emergency_reports) + 1, "", "", student_id, time.time(), "")
                    emergency_report.make_report()
                    emergency_reports.append(emergency_report)
                    print(f"Emergency report ID: {emergency_report.get_report_id()} \nThe account has been logged out!\n")
                else:
                    print(f"Student with ID {student_id} not found. Register the account first.")

            elif choice == "3":
                # Update student information
                student_id = input("Enter student ID to update information: ")
                found_student = next((student for student in students if student.get_student_id() == student_id), None)

                if found_student:
                    found_student.update_information()
                else:
                    print(f"Student with ID {student_id} not found. Register the account first.")

            elif choice == "4":
                # Report Issue
                student_id = input("Enter student ID: ")
                password = input("Enter password: ")
                found_student = next((student for student in students if student.get_student_id() == student_id and student.get_password() == password), None)

                if found_student:
                    found_student.report_issue()
                else:
                    print(f"Student with ID {student_id} not found. Register the account first.")

            elif choice == "5":
                # Provide Feedback
                student_id = input("Enter student ID: ")
                password = input("Enter password: ")
                found_student = next((student for student in students if student.get_student_id() == student_id and student.get_password() == password), None)

                if found_student:
                    service_quality_feedback = input("Provide feedback on service quality: ")
                    satisfaction_rating = input("Rate your satisfaction (1-5): ")

                    if satisfaction_rating.isdigit() and 1 <= int(satisfaction_rating) <= 5:
                        found_student.CollectFeedback(service_quality_feedback, int(satisfaction_rating))
                        print("Feedback submitted successfully.")
                    else:
                        print("Invalid satisfaction rating. Please enter a number between 1 and 5.")
                else:
                    print(f"Student with ID {student_id} not found. Register the account first.")

            elif choice == "6":
                # Exit student menu
                print("Exiting student menu.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                
    elif user_choice == "2":
        if admin_instance.Login():
            while True:
                print("\nAdmin Menu:")
                print("1. Update emergency report:")
                print("2. View all student information and reports:")
                print("3. View all feedback:")
                print("4. Exit:")
                admin_choice = input("Select an option 1-4:")
                
                if admin_choice == '1':
                    
                    # Update emergency report
                    report_id = input("Enter emergency report ID to update status: ")
                    found_report = next((report for report in emergency_reports if report.get_report_id() == int(report_id)), None)

                    if found_report:
                        found_report.update_status("Settled")
                        
                    else:
                        print(f"Emergency report with ID {report_id} not found.") 
                
                elif admin_choice == '2':
                    # View all student information and reports 
                    print("\nStudent Information:") 
                    for student in students: 
                        print(f"Student ID: {student.get_student_id()}, Name: {student.get_student_name()}, Email: {student.get_student_email()}, Contact Number: {student.get_student_contact_number()}") 
                        for report in emergency_reports: 
                            report.display_emergency_report()
                            
                elif admin_choice == '3':
                    # View All Feedback
                    print("\nAll Feedback:")
                    for student in students:
                        print(f"\nFeedback for {student.get_student_name()}")
                        print("-----------------------------------------------------")
                        for feedback_entry in student.feedback_collection:
                            print(f"Service Quality Feedback: {feedback_entry['ServiceQualityFeedback']}")
                            print(f"Satisfaction Rating: {feedback_entry['SatisfactionRating']}\n")

                elif admin_choice == '4':
                    # Exit admin menu
                     print("Exiting admin menu.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
    
    elif user_choice == '3':  # Housing College Administrator Menu
        if housing_admin_instance.LogIn():
            while True:
                print("\nHousing College Administrator Menu:")
                print("1. Schedule Maintenance")
                print("2. Assign Issue")
                print("3. Log out")

                housing_admin_choice = input("Select an option 1-3: ")
                
                if housing_admin_choice == '1':
                   # Schedule Maintenance
                   student_id = input("Enter student ID: ")
                   found_student = next((student for student in students if student.get_student_id() == student_id), None) 
                   if found_student:
                        issue_description = input("Enter issue description: ")
                        housing_admin_instance.ScheduleMaintenance(found_student, issue_description)
                   else:
                        print(f"Student with ID {student_id} not found.")
                
                if housing_admin_choice == '2':
                   housing_admin_instance.assign_issue_menu(emergency_reports, maintenance_teams)
                   
                elif housing_admin_choice == '3':
                    # Logout from Housing College Administrator Menu
                    print("-----------------------------------------------------")
                    print("Logged out from Housing College Administrator Menu.")
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
                    
    elif user_choice == "4":
        maintenanceTeamMainPage()
        
    elif user_choice == "5":
        # Exit the program
        print("Exiting the program.Thanks for using this system, goodbye (^_^)!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")