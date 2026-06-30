# This code is written by Bibek Acharya
# Student ID: 20251509
# BACT7501 Assessment 2 - Requisition System using OOP
class Requisition:

    # Class variables for tracking requisition information
    next_requisition_id = 10001

    total_requisitions = 0
    approved_requisitions = 0
    pending_requisitions = 0
    not_approved_requisitions = 0

    # Constructor method
    def __init__(self, date, staff_id, staff_name):

        # Initializing requisition details
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name

        # Generating unique requisition ID
        self.requisition_id = Requisition.next_requisition_id
        Requisition.next_requisition_id += 1

        # Initializing requisition data
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

        # Increasing total requisition count
        Requisition.total_requisitions += 1

    # Method for adding requisition items
    def add_requisition(self):

        while True:

            # Getting item details from user
            item_name = input("Enter item name: ")
            item_cost = float(input("Enter item cost: $"))

            # Adding item to list
            self.items.append((item_name, item_cost))

            # Calculating total cost
            self.total += item_cost

            choice = input("Do you want to add another item? (yes/no): ").lower()

            if choice == "no":
                break

        # Calling approval method
        self.approve_requisition()

    # Method to automatically approve requisition
    def approve_requisition(self):
        
        # Requisitions below $500 are approved
        if self.total < 500:

            self.status = "Approved"

            # Creating approval reference number
            last_three_digits = str(self.requisition_id)[-3:]
            self.approval_reference = self.staff_id + last_three_digits

            Requisition.approved_requisitions += 1

        else:

            # Requisitions $500 or more remain pending
            self.status = "Pending"
            self.approval_reference = "Not available"

            Requisition.pending_requisitions += 1

    # Method for manager response
    def respond_requisition(self):

        if self.status == "Pending":

            print("\nManager Response Required")
            print("1. Approve")
            print("2. Not Approve")
            print("3. Leave as Pending")

            choice = input("Enter your choice: ")
            

            if choice == "1":

                self.status = "Approved"

                # Creating approval reference number
                last_three_digits = str(self.requisition_id)[-3:]
                self.approval_reference = self.staff_id + last_three_digits

                Requisition.pending_requisitions -= 1
                Requisition.approved_requisitions += 1

            elif choice == "2":

                self.status = "Not approved"
                self.approval_reference = "Not available"

                Requisition.pending_requisitions -= 1
                Requisition.not_approved_requisitions += 1

            elif choice == "3":

                print("Requisition remains Pending")

            else:

                print("Invalid choice")

    # Method to display requisition information
    def display_requisition(self):

        print("\nDate:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $" + str(self.total))
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)
        print("-------------------------------------------------------------------------------------------------------------")

    # Method to display requisition statistics
    def requisition_statistics(self):

        print("\nDisplaying the Requisition Statistics")
        print("The total number of requisitions submitted:", Requisition.total_requisitions)
        print("The total number of approved requisitions:", Requisition.approved_requisitions)
        print("The total number of pending requisitions:", Requisition.pending_requisitions)
        print("The total number of not approved requisitions:", Requisition.not_approved_requisitions)


# ==========================
# Main Program Starts Here
# ==========================

# Creating list to store requisition objects 
requisition_list = []

print("Welcome to Requisition System")

# Getting number of requisitions
number = int(input("How many requisitions do you want to enter? "))

# Loop for creating requisitions
for i in range(number):

    print("\nEnter details for Requisition", i + 1)

    date = input("Enter Date: ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")

    # Creating object
    req = Requisition(date, staff_id, staff_name)

    # Adding requisition items
    req.add_requisition()

    # Storing object in list
    requisition_list.append(req)

# Displaying requisitions before manager response
print("\nREQUISITION INFORMATION BEFORE MANAGER RESPONSE")

for req in requisition_list:
    req.display_requisition()

# Displaying statistics
if len(requisition_list) > 0:
    requisition_list[0].requisition_statistics()

# Manager responds to pending requisitions
print("\nManager will now respond to pending requisitions.")

for req in requisition_list:
    req.respond_requisition()

# Displaying final requisition information
print("\nREQUISITION INFORMATION AFTER MANAGER RESPONSE")

for req in requisition_list:
    req.display_requisition()

# Displaying updated statistics
if len(requisition_list) > 0:
    requisition_list[0].requisition_statistics()