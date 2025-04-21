
# 🚗 Parking Management System

A robust and role-based Parking Management System developed using **Python** and **MySQL**, designed to automate parking operations like vehicle entry/exit, slot tracking, employee management, and real-time billing.

---

## 📌 Features

### 🔒 Employee Login & Role Management
- Secure login using ID & password.
- Role-based access control:
  - **Security Guard** – View data.
  - **Parking Supervisor** – Manage parking slots.
  - **Parking Manager** – Full access (slots + employees).
  - **Tech Support** – View logs.

### 🚘 Parking Slot Management
- Add/Delete/Update slot info.
- Check real-time slot availability.
- Auto-assign slots based on size (Small/Medium/Large).
- Update vacancy status on vehicle exit.

### 🧾 Billing System
- Charges based on slot size & duration:
  - Small: ₹0.50/sec
  - Medium: ₹0.75/sec
  - Large: ₹1.00/sec
- Bill generation and storage in the database.

### 👥 Employee Control
- Add/Update/Delete employee records.
- Logs all activities (login/logout, modifications).

### 📊 Data Reporting
- Export data statements between dates to CSV.
- Track parking history and employee logs.

---

## 🛠️ Tech Stack

- **Python** – Backend Logic
- **MySQL** – Data Storage
- **CSV** – Exporting reports
- **datetime module** – Time tracking

---

## ⚙️ How It Works

1. **Start the Program**
   - Prompts for car number or `"employee"` for login.

2. **Car Entry**
   - Enter car number and required slot size.
   - System allocates and logs the entry.

3. **Car Exit**
   - Enter car number again.
   - Calculates bill and frees the slot.

4. **Employee Login**
   - Enter credentials and access menu based on role.

---

## 🔄 Workflow Examples

### General User
```bash
> enter your car number : DL 01 CS 5678
> enter the parking size you require : large
# Allocated: Pillar 1, Slot 11

> enter your car number : DL 01 CS 5678
# Bill: ₹16
```

### Employee
```bash
> enter your car number : employee
> employee id : EMP003
> password : pass3
# Login successful

# Choose option: Add slot
# Slot 78 added successfully

# Choose option: Get data statement
# CSV saved to directory
```

---

## 📂 Database Structure

### `parking_inventory`
| Column      | Description        |
|-------------|--------------------|
| slot_no     | Slot Number        |
| pillar_no   | Pillar Number      |
| size        | Small/Medium/Large |
| availability| TRUE/FALSE         |

### `parking_records`
| Column       | Description         |
|--------------|---------------------|
| entry_time   | Entry Timestamp     |
| leaving_time | Exit Timestamp      |
| car_no       | Car Number          |
| slot_no      | Slot Allocated      |
| bill_generated | Amount Charged    |

### `employee_logs`
| Column       | Description         |
|--------------|---------------------|
| emp_id       | Employee ID         |
| role         | Designation         |
| login_time   | Login Timestamp     |
| logout_time  | Logout Timestamp    |

---

## 🛠️ Future Improvements
- Web-based UI using Flask/Django.
- Real-time notifications for slot status.
- Payment gateway integration.
- Graphical dashboard for analytics.

---

## 📚 References
- *Computer Science with Python* – Preeti Arora
- *Computer Science with Python* – Sumita Arora
- [Python Docs](https://docs.python.org)
- [Google](https://www.google.com)
- *Python Distilled*

---

## 👨‍💻 Author

**Shubham Panwar**  


---

> 💡 *"Park smart. Manage smarter."*
