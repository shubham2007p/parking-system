import employees as e
import parking_inventory as p
import datetime as dt


def entering_in_parking():
    try:
        response = p.availability(slot_size)
        if response[0]:
            pillar_no, slot_no = response[2], response[1]
            entry_time = dt.datetime.now()
            parked_cars.append([car_number, pillar_no, slot_no, entry_time])
            print("parking size is available")
            print(f"Your parking co-ordinates are pillar no. {pillar_no} and slot no. {slot_no}")
    except Exception as err:
        print(err)


def bill_genrating(leaving_time, entry_time, slot_no, car_no):
    try:

        parked_time = (leaving_time - entry_time).total_seconds()
        if slot_size.lower() == "small":
            total_bill = 0.50 * parked_time
        elif slot_size.lower() == "medium":
            total_bill = 0.75 * parked_time
        elif slot_size.lower() == "large":
            total_bill = 1.0 * parked_time

        print("₹" + str(int(total_bill)))
        history(entry_time, leaving_time, car_no, slot_no, total_bill)
    except Exception as err:
        print(err)


def history(entry_time, leaving_time, car_no, slot_no, bill_generated):
    response = p.parking_records(entry_time, leaving_time, car_no, slot_no, bill_generated)
    print(response)


def leaving_from_parking(car_no, pillar_no, slot_no, entry_time):
    p.vacancy(pillar_no, slot_no)
    leaving_time = dt.datetime.now()
    bill_genrating(leaving_time, entry_time, slot_no, car_no)


parked_cars = []
while True:
    car_number = input("enter your car number : ")
    if car_number == "employee":
        e.login()
    else:

        for entries in parked_cars:
            if car_number == entries[0]:
                leaving_from_parking(entries[0], entries[1], entries[2], entries[3])
                break
        else:
            slot_size = input("enter the parking size you require : ")
            entering_in_parking()
