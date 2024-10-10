import mysql.connector as m
import csv

db = m.connect(user="root", host="localhost", password="system@2007", database="parking")
db_cursor = db.cursor()


def availability(slot_size):
    empty = ()
    try:
        db_cursor.execute("SELECT * FROM parking_inventory WHERE UPPER(size) = UPPER(%s) AND availability = TRUE;",
                          (slot_size,))
        i = db_cursor.fetchall()
        result = i[0]
        return_object = (True, result[0], result[1])
        if result != empty:
            db_cursor.execute(
                "update parking_inventory set availability = FALSE where slot_no = %s and pillar_no = %s ;",
                (result[0], result[1],))
            return return_object
        else:
            return "Parking size isn't available right now"
    except Exception as err:
        print(err)


def vacancy(pillar_no, slot_no):
    db_cursor.execute("update parking_inventory set availability = TRUE where pillar_no = %s and slot_no = %s ;",
                      (pillar_no, slot_no,))


def parking_records(entry_time, leaving_time, car_no, slot_no, bill):
    db_cursor.execute("INSERT INTO parking_records  VALUES (%s, %s, %s, %s, %s)",
                      (entry_time, leaving_time, car_no, slot_no, bill))
    db.commit()

    return "have a great day"


def employee_records(act_rec):
    db_cursor.execute("insert into employee_logs Values (%s,%s,%s,%s,%s);",
                      (act_rec[0], act_rec[2], act_rec[1], act_rec[3], act_rec[4]))
    return True


def data(start, end):
    db_cursor.execute("SELECT * FROM parking_records WHERE entry_time BETWEEN %s AND %s;", (start, end,))
    results = db_cursor.fetchall()
    coulmns = []
    with open(
            fr'C:\Users\shubh\Downloads\cs all codes\project (parking system)\file created\data_statment_{start}_to_{end}.csv',
            'w', newline='') as f:
        # potential error
        writer = csv.writer(f)
        db_cursor.execute("describe parking_records")
        for i in db_cursor.fetchall():
            coulmns.append(i[0])
        writer.writerow(coulmns)
        writer.writerows(results)

        return "the data statement is in directory"


def add(slot_no, pillar_no, size):
    db_cursor.execute("INSERT INTO parking_inventory VALUES (%s,%s,%s,1);", (slot_no, pillar_no, size,))
    db_cursor.execute("select * from parking_inventory where slot_no = %s ;", slot_no)
    r = db_cursor.fetchone()
    if r[0] == slot_no:
        return True
    else:
        return False


def dlt(slot_no):
    db_cursor.execute("DELETE FROM parking_inventory WHERE slot_no = %s;", slot_no)
    db_cursor.execute("select * from parking_inventory where slot_no = %s ;", slot_no)
    r = db_cursor.fetchone()
    if r:
        return False
    else:
        return True


def size_updation(size, slot_no):
    db_cursor.execute("update parking_inventory set size = %s where slot_no = %s ;", (size, slot_no))
    return True


def pillar_no_updation(pillar_no, slot_no):
    db_cursor.execute("update parking_inventory set pillar_no = %s where slot_no = %s ;", (pillar_no, slot_no))
