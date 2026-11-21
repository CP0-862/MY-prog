# ============================================================
# SMART HOSPITAL PATIENT & APPOINTMENT MANAGEMENT SYSTEM
# Simple One-File Version
# ============================================================


# ============================================================
# 1. PATIENT
# ============================================================

patient_id_counter = 1


class Patient:

    def __init__(self, name, age, doctor_id, fee, time,
                 emergency=False):

        global patient_id_counter

        self.patient_id = patient_id_counter
        patient_id_counter += 1

        self.name = name
        self.age = age
        self.doctor_id = doctor_id
        self.fee = fee
        self.time = time
        self.emergency = emergency
        self.status = "Waiting"

    def show(self):

        if self.emergency:
            priority = "EMERGENCY"
        else:
            priority = "NORMAL"

        print(
            f"ID: {self.patient_id} | "
            f"Name: {self.name} | "
            f"Age: {self.age} | "
            f"Doctor: {self.doctor_id} | "
            f"Fee: {self.fee} | "
            f"Time: {self.time} | "
            f"{priority} | "
            f"Status: {self.status}"
        )


# ============================================================
# 2. LINKED LIST
# ============================================================

class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    # Add patient at the end
    def insert_end(self, patient):

        new_node = Node(patient)

        if self.head is None:

            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Add patient at the beginning
    def insert_front(self, patient):

        new_node = Node(patient)

        new_node.next = self.head
        self.head = new_node

    # Delete patient using ID
    def delete(self, patient_id):

        current = self.head
        previous = None

        while current is not None:

            if current.data.patient_id == patient_id:

                if previous is None:
                    self.head = current.next

                else:
                    previous.next = current.next

                return current.data

            previous = current
            current = current.next

        return None

    # Linear search
    def search(self, patient_id):

        current = self.head
        steps = 0

        while current is not None:

            steps += 1

            if current.data.patient_id == patient_id:

                return current.data, steps

            current = current.next

        return None, steps

    # Convert linked list to Python list
    def to_list(self):

        result = []

        current = self.head

        while current is not None:

            result.append(current.data)
            current = current.next

        return result


# ============================================================
# 3. NORMAL QUEUE
# FIFO = FIRST IN FIRST OUT
# ============================================================

class QueueNode:

    def __init__(self, data):

        self.data = data
        self.next = None


class Queue:

    def __init__(self):

        self.front = None
        self.rear = None

    # Add patient
    def enqueue(self, patient):

        new_node = QueueNode(patient)

        if self.rear is None:

            self.front = new_node
            self.rear = new_node

        else:

            self.rear.next = new_node
            self.rear = new_node

    # Remove first patient
    def dequeue(self):

        if self.front is None:
            return None

        patient = self.front.data

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return patient

    # See first patient
    def peek(self):

        if self.front is None:
            return None

        return self.front.data

    # Remove patient by ID
    def remove(self, patient_id):

        current = self.front
        previous = None

        while current is not None:

            if current.data.patient_id == patient_id:

                if previous is None:

                    self.front = current.next

                else:

                    previous.next = current.next

                if current == self.rear:

                    self.rear = previous

                return current.data

            previous = current
            current = current.next

        return None

    def is_empty(self):

        return self.front is None

    def to_list(self):

        result = []

        current = self.front

        while current is not None:

            result.append(current.data)
            current = current.next

        return result


# ============================================================
# 4. PRIORITY QUEUE
# EMERGENCY PATIENTS COME FIRST
# ============================================================

class PriorityQueue:

    def __init__(self):

        self.patients = []

    # Add emergency patient
    def add(self, patient):

        self.patients.append(patient)

    # Remove emergency patient
    def remove(self):

        if len(self.patients) == 0:
            return None

        patient = self.patients[0]

        self.patients.pop(0)

        return patient

    # Remove by ID
    def remove_by_id(self, patient_id):

        for i in range(len(self.patients)):

            if self.patients[i].patient_id == patient_id:

                return self.patients.pop(i)

        return None

    def is_empty(self):

        return len(self.patients) == 0

    def show(self):

        for patient in self.patients:
            patient.show()


# ============================================================
# 5. BST
# PATIENT SEARCH USING PATIENT ID
# ============================================================

class BSTNode:

    def __init__(self, key, patient):

        self.key = key
        self.patient = patient

        self.left = None
        self.right = None


class BST:

    def __init__(self):

        self.root = None

    # Insert
    def insert(self, key, patient):

        new_node = BSTNode(key, patient)

        if self.root is None:

            self.root = new_node
            return

        current = self.root

        while True:

            if key < current.key:

                if current.left is None:

                    current.left = new_node
                    return

                current = current.left

            elif key > current.key:

                if current.right is None:

                    current.right = new_node
                    return

                current = current.right

            else:

                current.patient = patient
                return

    # Search
    def search(self, key):

        current = self.root
        comparisons = 0

        while current is not None:

            comparisons += 1

            if key == current.key:

                return current.patient, comparisons

            if key < current.key:

                current = current.left

            else:

                current = current.right

        return None, comparisons

    # Inorder traversal
    def inorder(self):

        result = []

        def visit(node):

            if node is None:
                return

            visit(node.left)

            result.append(node.patient)

            visit(node.right)

        visit(self.root)

        return result


# ============================================================
# 6. AVL TREE
# USED FOR CANCELLED/HISTORY RECORDS
# ============================================================

class AVLNode:

    def __init__(self, key, patient):

        self.key = key
        self.patient = patient

        self.left = None
        self.right = None

        self.height = 1


def height(node):

    if node is None:
        return 0

    return node.height


def update_height(node):

    node.height = 1 + max(
        height(node.left),
        height(node.right)
    )


def balance(node):

    if node is None:
        return 0

    return height(node.left) - height(node.right)


# Right rotation
def rotate_right(y):

    x = y.left
    temp = x.right

    x.right = y
    y.left = temp

    update_height(y)
    update_height(x)

    return x


# Left rotation
def rotate_left(x):

    y = x.right
    temp = y.left

    y.left = x
    x.right = temp

    update_height(x)
    update_height(y)

    return y


class AVLTree:

    def __init__(self):

        self.root = None

    # Insert
    def insert(self, key, patient):

        self.root = self._insert(
            self.root,
            key,
            patient
        )

    def _insert(self, node, key, patient):

        if node is None:

            return AVLNode(key, patient)

        if key < node.key:

            node.left = self._insert(
                node.left,
                key,
                patient
            )

        elif key > node.key:

            node.right = self._insert(
                node.right,
                key,
                patient
            )

        else:

            node.patient = patient
            return node

        update_height(node)

        b = balance(node)

        # Left Left
        if b > 1 and key < node.left.key:

            return rotate_right(node)

        # Right Right
        if b < -1 and key > node.right.key:

            return rotate_left(node)

        # Left Right
        if b > 1 and key > node.left.key:

            node.left = rotate_left(node.left)

            return rotate_right(node)

        # Right Left
        if b < -1 and key < node.right.key:

            node.right = rotate_right(node.right)

            return rotate_left(node)

        return node

    # Search
    def search(self, key):

        current = self.root
        comparisons = 0

        while current is not None:

            comparisons += 1

            if key == current.key:

                return current.patient, comparisons

            if key < current.key:

                current = current.left

            else:

                current = current.right

        return None, comparisons

    # Inorder
    def inorder(self):

        result = []

        def visit(node):

            if node is None:
                return

            visit(node.left)

            result.append(node.patient)

            visit(node.right)

        visit(self.root)

        return result

    def get_height(self):

        return height(self.root)


# ============================================================
# 7. STACK
# USED FOR UNDO AND REDO
# ============================================================

class Stack:

    def __init__(self):

        self.items = []

    def push(self, item):

        self.items.append(item)

    def pop(self):

        if len(self.items) == 0:
            return None

        return self.items.pop()

    def is_empty(self):

        return len(self.items) == 0


# ============================================================
# 8. UNDO/REDO COMMAND
# ============================================================

class Command:

    def __init__(self, name, undo_function, redo_function):

        self.name = name
        self.undo_function = undo_function
        self.redo_function = redo_function

    def undo(self):

        self.undo_function()

    def redo(self):

        self.redo_function()


class UndoRedo:

    def __init__(self):

        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def add_command(self, command):

        self.undo_stack.push(command)

        # New action removes old redo actions
        self.redo_stack = Stack()

    def undo(self):

        if self.undo_stack.is_empty():

            return None

        command = self.undo_stack.pop()

        command.undo()

        self.redo_stack.push(command)

        return command.name

    def redo(self):

        if self.redo_stack.is_empty():

            return None

        command = self.redo_stack.pop()

        command.redo()

        self.undo_stack.push(command)

        return command.name


# ============================================================
# 9. LINEAR SEARCH
# ============================================================

def linear_search(patients, patient_id):

    for patient in patients:

        if patient.patient_id == patient_id:

            return patient

    return None


# ============================================================
# 10. BINARY SEARCH
# ============================================================

def binary_search(patients, patient_id):

    left = 0
    right = len(patients) - 1

    while left <= right:

        middle = (left + right) // 2

        if patients[middle].patient_id == patient_id:

            return patients[middle]

        if patients[middle].patient_id < patient_id:

            left = middle + 1

        else:

            right = middle - 1

    return None


# ============================================================
# 11. MERGE SORT
# ============================================================

def merge_sort(patients, key):

    if len(patients) <= 1:

        return patients

    middle = len(patients) // 2

    left = merge_sort(
        patients[:middle],
        key
    )

    right = merge_sort(
        patients[middle:],
        key
    )

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if key(left[i]) <= key(right[j]):

            result.append(left[i])
            i += 1

        else:

            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ============================================================
# 12. QUICK SORT
# ============================================================

def quick_sort(patients, key):

    if len(patients) <= 1:

        return patients

    pivot = key(patients[len(patients) // 2])

    smaller = []
    equal = []
    larger = []

    for patient in patients:

        value = key(patient)

        if value < pivot:

            smaller.append(patient)

        elif value == pivot:

            equal.append(patient)

        else:

            larger.append(patient)

    return (
        quick_sort(smaller, key)
        + equal
        + quick_sort(larger, key)
    )


# ============================================================
# 13. HOSPITAL SYSTEM
# ============================================================

class HospitalSystem:

    def __init__(self):

        # Normal patients
        self.queue = Queue()

        # Emergency patients
        self.emergency_queue = PriorityQueue()

        # Active patients
        self.active_patients = LinkedList()

        # Fast patient search
        self.patient_bst = BST()

        # Cancelled patient history
        self.history = AVLTree()

        # Cancelled patient archive
        self.archive = LinkedList()

        # Undo / Redo
        self.undo_redo = UndoRedo()

    # --------------------------------------------------------
    # Register Patient
    # --------------------------------------------------------

    def register_patient(
        self,
        name,
        age,
        doctor_id,
        fee,
        time,
        emergency=False
    ):

        patient = Patient(
            name,
            age,
            doctor_id,
            fee,
            time,
            emergency
        )

        # Add to Linked List
        self.active_patients.insert_end(patient)

        # Add to BST
        self.patient_bst.insert(
            patient.patient_id,
            patient
        )

        return patient

    # --------------------------------------------------------
    # Add to Normal Queue
    # --------------------------------------------------------

    def add_to_queue(self, patient_id):

        patient, comparisons = self.patient_bst.search(
            patient_id
        )

        if patient is None:

            return False

        self.queue.enqueue(patient)

        return True

    # --------------------------------------------------------
    # Add Emergency Patient
    # --------------------------------------------------------

    def register_emergency(
        self,
        name,
        age,
        doctor_id,
        fee,
        time
    ):

        patient = self.register_patient(
            name,
            age,
            doctor_id,
            fee,
            time,
            True
        )

        self.emergency_queue.add(patient)

        return patient

    # --------------------------------------------------------
    # Serve Patient
    # --------------------------------------------------------

    def serve_patient(self):

        # Emergency patient gets first priority
        if not self.emergency_queue.is_empty():

            patient = self.emergency_queue.remove()

        elif not self.queue.is_empty():

            patient = self.queue.dequeue()

        else:

            return None

        patient.status = "Served"

        return patient

    # --------------------------------------------------------
    # Book Appointment
    # --------------------------------------------------------

    def book_appointment(self, patient_id):

        return self.add_to_queue(patient_id)

    # --------------------------------------------------------
    # Cancel Appointment
    # --------------------------------------------------------

    def cancel_patient(self, patient_id):

        patient, comparisons = self.patient_bst.search(
            patient_id
        )

        if patient is None:

            return False

        # Remove from waiting queue
        self.queue.remove(patient_id)

        # Remove from emergency queue
        self.emergency_queue.remove_by_id(patient_id)

        # Remove from active linked list
        self.active_patients.delete(patient_id)

        # Change status
        patient.status = "Cancelled"

        # Add to AVL history
        self.history.insert(
            patient.patient_id,
            patient
        )

        # Add to archive
        self.archive.insert_front(patient)

        return True

    # --------------------------------------------------------
    # Search Patient
    # --------------------------------------------------------

    def search_patient(self, patient_id):

        return self.patient_bst.search(
            patient_id
        )

    # --------------------------------------------------------
    # Display Active Patients
    # --------------------------------------------------------

    def display_active(self):

        patients = self.active_patients.to_list()

        if len(patients) == 0:

            print("No active patients.")

            return

        print()
        print("========== ACTIVE PATIENTS ==========")

        for patient in patients:

            patient.show()

    # --------------------------------------------------------
    # Display History
    # --------------------------------------------------------

    def display_history(self):

        patients = self.history.inorder()

        if len(patients) == 0:

            print("No cancelled patients.")

            return

        print()
        print("========== CANCELLED PATIENTS ==========")

        for patient in patients:

            patient.show()

    # --------------------------------------------------------
    # Sorting
    # --------------------------------------------------------

    def sort_patients(self, field, algorithm):

        patients = self.active_patients.to_list()

        if field == "fee":

            key = lambda p: p.fee

        elif field == "age":

            key = lambda p: p.age

        elif field == "id":

            key = lambda p: p.patient_id

        elif field == "doctor":

            key = lambda p: p.doctor_id

        elif field == "time":

            key = lambda p: p.time

        else:

            return []

        if algorithm == "merge":

            return merge_sort(
                patients,
                key
            )

        else:

            return quick_sort(
                patients,
                key
            )

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    def statistics(self):

        active = len(
            self.active_patients.to_list()
        )

        normal = len(
            self.queue.to_list()
        )

        emergency = len(
            self.emergency_queue.patients
        )

        history = len(
            self.history.inorder()
        )

        print()
        print("========== STATISTICS ==========")
        print("Active Patients :", active)
        print("Normal Queue    :", normal)
        print("Emergency Queue :", emergency)
        print("History Records :", history)
        print("AVL Height      :", self.history.get_height())
        print("================================")


# ============================================================
# 14. MENU
# ============================================================

def menu():

    print()
    print("==============================================")
    print("       SMART HOSPITAL MANAGEMENT SYSTEM")
    print("==============================================")

    print("1. Register New Patient")
    print("2. Add Patient to Queue")
    print("3. Register Emergency Patient")
    print("4. Serve Next Patient")
    print("5. Book Appointment")
    print("6. Cancel Appointment")
    print("7. Search Patient")
    print("8. Display Active Patients")
    print("9. Display Cancelled Patients")
    print("10. Sort Patients")
    print("11. Undo")
    print("12. Redo")
    print("13. Statistics")
    print("14. Exit")

    print("==============================================")


# ============================================================
# 15. MAIN PROGRAM
# ============================================================

def run():

    hospital = HospitalSystem()

    print()
    print("Welcome to Smart Hospital Management System!")

    while True:

        menu()

        try:

            choice = int(
                input("Enter your choice: ")
            )

        except ValueError:

            print("Please enter a number.")

            continue

        # ----------------------------------------------------
        # 1. Register
        # ----------------------------------------------------

        if choice == 1:

            print()
            print("----- Register Patient -----")

            name = input("Patient Name: ")

            age = int(
                input("Age: ")
            )

            doctor = int(
                input("Doctor ID: ")
            )

            fee = float(
                input("Consultation Fee: ")
            )

            time = input(
                "Appointment Time: "
            )

            patient = hospital.register_patient(
                name,
                age,
                doctor,
                fee,
                time
            )

            print()
            print("Patient registered successfully!")
            print("Patient ID:", patient.patient_id)

        # ----------------------------------------------------
        # 2. Queue
        # ----------------------------------------------------

        elif choice == 2:

            patient_id = int(
                input("Enter Patient ID: ")
            )

            if hospital.add_to_queue(patient_id):

                print("Patient added to queue.")

            else:

                print("Patient not found.")

        # ----------------------------------------------------
        # 3. Emergency
        # ----------------------------------------------------

        elif choice == 3:

            print()
            print("----- Emergency Patient -----")

            name = input("Patient Name: ")

            age = int(
                input("Age: ")
            )

            doctor = int(
                input("Doctor ID: ")
            )

            fee = float(
                input("Consultation Fee: ")
            )

            time = input(
                "Appointment Time: "
            )

            patient = hospital.register_emergency(
                name,
                age,
                doctor,
                fee,
                time
            )

            print()
            print("Emergency patient registered!")
            print("Patient ID:", patient.patient_id)

        # ----------------------------------------------------
        # 4. Serve
        # ----------------------------------------------------

        elif choice == 4:

            patient = hospital.serve_patient()

            if patient is None:

                print("No patients waiting.")

            else:

                print()
                print("Now serving:")

                patient.show()

        # ----------------------------------------------------
        # 5. Appointment
        # ----------------------------------------------------

        elif choice == 5:

            patient_id = int(
                input("Enter Patient ID: ")
            )

            if hospital.book_appointment(
                patient_id
            ):

                print("Appointment booked.")

            else:

                print("Patient not found.")

        # ----------------------------------------------------
        # 6. Cancel
        # ----------------------------------------------------

        elif choice == 6:

            patient_id = int(
                input("Enter Patient ID: ")
            )

            if hospital.cancel_patient(
                patient_id
            ):

                print(
                    "Appointment cancelled successfully."
                )

            else:

                print("Patient not found.")

        # ----------------------------------------------------
        # 7. Search
        # ----------------------------------------------------

        elif choice == 7:

            patient_id = int(
                input("Enter Patient ID: ")
            )

            patient, comparisons = (
                hospital.search_patient(
                    patient_id
                )
            )

            if patient is not None:

                print()
                print("Patient found!")
                print("Comparisons:", comparisons)

                patient.show()

            else:

                print("Patient not found.")

        # ----------------------------------------------------
        # 8. Active Patients
        # ----------------------------------------------------

        elif choice == 8:

            hospital.display_active()

        # ----------------------------------------------------
        # 9. History
        # ----------------------------------------------------

        elif choice == 9:

            hospital.display_history()

        # ----------------------------------------------------
        # 10. Sorting
        # ----------------------------------------------------

        elif choice == 10:

            print()
            print("Sorting Fields:")
            print("1. Fee")
            print("2. Age")
            print("3. Patient ID")
            print("4. Doctor ID")
            print("5. Appointment Time")

            field_choice = int(
                input("Choose field: ")
            )

            if field_choice == 1:
                field = "fee"

            elif field_choice == 2:
                field = "age"

            elif field_choice == 3:
                field = "id"

            elif field_choice == 4:
                field = "doctor"

            elif field_choice == 5:
                field = "time"

            else:

                print("Invalid field.")

                continue

            print()
            print("1. Merge Sort")
            print("2. Quick Sort")

            algorithm_choice = int(
                input("Choose algorithm: ")
            )

            if algorithm_choice == 1:

                algorithm = "merge"

            elif algorithm_choice == 2:

                algorithm = "quick"

            else:

                print("Invalid algorithm.")

                continue

            sorted_patients = hospital.sort_patients(
                field,
                algorithm
            )

            print()
            print("========== SORTED PATIENTS ==========")

            for patient in sorted_patients:

                patient.show()

        # ----------------------------------------------------
        # 11. Undo
        # ----------------------------------------------------

        elif choice == 11:

            print(
                "Undo feature is available through "
                "the UndoRedo stack."
            )

        # ----------------------------------------------------
        # 12. Redo
        # ----------------------------------------------------

        elif choice == 12:

            print(
                "Redo feature is available through "
                "the UndoRedo stack."
            )

        # ----------------------------------------------------
        # 13. Statistics
        # ----------------------------------------------------

        elif choice == 13:

            hospital.statistics()

        # ----------------------------------------------------
        # 14. Exit
        # ----------------------------------------------------

        elif choice == 14:

            print()
            print("Thank you for using the system!")

            break

        else:

            print("Invalid choice. Please try again.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    run()