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