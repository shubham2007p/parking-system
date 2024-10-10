import datetime as dt
import parking_inventory as p


def get_employee_info():
    return employees


employees = {
    "EMP001": ["Rahul", "pass1", "Security Guard"],  # ONLY DATA STATEMENTS
    "EMP002": ["Priya", "pass2", "Parking Supervisor"],  # ADDING REMOVING SPACE
    "EMP003": ["Amit", "pass3", "Parking Manager"],  # ALL ACCESS
    "EMP004": ["Neha", "pass4", "Parking Cleaner"],
    "EMP005": ["Ashish", "pass5", "Security Guard"],  # ONLY DATA STATEMENTS
    "EMP006": ["Anjali", "pass6", "Security Guard"],  # ONLY DATA STATEMENTS
    "EMP007": ["Vivek", "pass7", "Parking Supervisor"],  # ADDING REMOVING SPACE
    "EMP008": ["Ramesh", "pass8", "Parking Cleaner"],
    "EMP009": ["Suresh", "pass9", "Security Guard"],  # ONLY DATA STATEMENTS
    "EMP010": ["Meena", "pass10", "Parking Supervisor"],  # ADDING REMOVING SPACE
    "EMP011": ["Rajesh", "pass11", "Parking Cleaner"],
    "EMP012": ["Sunita", "pass12", "Parking Cleaner"]
}

act_records = []
changes = []

permissions = {
    "Security Guard": ["view_data"],
    "Parking Supervisor": ["add_parking_space", "remove_parking_space", "view_data"],
    "Parking Manager": ["manage_parking_system", "view_reports"],
    "Parking Tech Person": ["view_data"]
}


def login():
    try:
        emp_id = input("enter your employee id : ")
        pass_key = input("password : ")
        for entries in employees.keys():
            if emp_id in entries:
                details = employees[emp_id]
                if pass_key == details[1]:
                    print("login successfully")
                    # global loged_in_time
                    loged_in_time = dt.datetime.now()
                    act_records.extend(emp_id, loged_in_time)
                    menu(emp_id)
                    break
                else:
                    print("password incorrect")
                    pass
            else:
                print("emp_id isn't correct or isn't in reccords")
    except Exception as err:
        print(err)


def slot_updation():
    act = input("U wanna add slot , dlt slot or update existing slot  ")
    try:

        if act == "add":
            slot_no = input(":")
            pillar_no = input(":")
            size = input(":")
            response = p.add(slot_no, pillar_no, size)
            if response:
                print("New slot added successfuly")
            else:
                print("Can't add new slot ")

        elif act == "dlt":
            slot_no = input("")
            response = p.dlt(slot_no)
            if response:
                print("Slot deleted successfuly")
            else:
                print("can't delet the slot")

        elif act == "update":
            slot_no = input("")
            change = input("what u want to chnage size or pillar no")
            if change in "size":
                size = input(" change to : ")
                p.size_updation(size, slot_no)
                print("successful")

            elif change in "pillar_no":
                pillar_no = input("change to : ")
                p.pillar_no_updation(pillar_no, slot_no)
                print("successful")
    except Exception as err:
        print(err)


def data_stat():
    print("For this feature u have to provide from date and to date eg.(2024-10-09)")
    from_date = input("enter the date from u want data : ")
    to_date = input("enter the date to u want data : ")
    response = p.data(from_date, to_date)
    print(response)


def emp_updation():
    act = input("U wanna add slot , dlt slot or update existing employee")
    try:
        if act == "add":
            name = input(":")
            designation = input(":")
            emp_id = input(":")
            pass_key = input(":")
            employees[emp_id] = [name, pass_key, designation]
            print(f"Employee name {name} with designation {designation} added successfuly")

        elif act == "dlt":
            emp_id = input(":")
            del employees[emp_id]
            print(f"Employee with emp_id {emp_id} is removed")

        elif act == "update":
            emp_id = input(":")
            try:
                change = input("change in what name passkey designation")
                if change == "name":
                    name = input(":")
                    r = employees[emp_id]
                    r[0] = name
                    employees[emp_id] = r

                elif change == "passkey":
                    passkey = input(":")
                    r = employees[emp_id]
                    r[1] = passkey
                    employees[emp_id] = r
                elif change == "designation":
                    designation = input(":")
                    r = employees[emp_id]
                    r[2] = designation
                    employees[emp_id] = r
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)


def temp():
    pass


# noinspection PyTypeChecker
def logout():
    confirm = input("are u aure about login out ?").lower()
    if confirm in ["y", "yes"]:
        loged_out_time = dt.datetime.now()
        act_records.extend(loged_out_time)
        p.employee_records(act_records)
        print("loged out successfuly")
        return


def menu(emp_id):
    while True:
        print("1. Modify parking slot size or information "
              "2. Get an data statement"
              "3. Add or modify employee information"
              "4. temp"
              "5. Log out")
        choice = int(input("Enter the choice : ")) - 1
        function_list = [slot_updation, data_stat, emp_updation, temp, logout]
        response = check_permissions(emp_id)
        if response:
            act = str(function_list)
            changes.append(act)
            function_list[choice]()
        else:
            print("U didn't have permission to do such changes")
        pass


def get_employee_role(emp_id):
    for entry in employees:
        if emp_id == entry[0]:
            return entry[2]
    return None


def check_permissions(emp_id, permission):
    role = get_employee_role(emp_id)
    act_records.append(role)
    if role and permission in permissions[role]:
        return True
    else:
        return False
