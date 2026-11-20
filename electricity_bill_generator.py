print("========== ELECTRICITY BILL GENERATOR ==========")
consumer_name = input("Enter Consumer Name: ")
consumer_id = input("Enter Consumer ID: ")
previous_reading = float(input("Enter Previous Meter Reading (kWh): "))
current_reading = float(input("Enter Current Meter Reading (kWh): "))
cost_per_unit = float(input("Enter Cost per Unit (Rs.): "))

if current_reading < previous_reading:
    print("Current meter reading cannot be less than the previous reading.")
elif cost_per_unit < 0:
    print("Cost per unit cannot be negative.")
else:
    units = current_reading - previous_reading
    energy_charge = units * cost_per_unit
    electricity_duty = energy_charge * 0.05
    fixed_charge = 100.0
    net_bill = energy_charge + electricity_duty + fixed_charge

    print("\n============== ELECTRICITY BILL ==============")
    print(f"Consumer Name : {consumer_name}")
    print(f"Consumer ID : {consumer_id}")
    print(f"Units Consumed : {units:.2f} kWh")
    print(f"Energy Charge : Rs.{energy_charge:.2f}")
    print(f"Electricity Duty (5%) : Rs.{electricity_duty:.2f}")
    print(f"Fixed Meter Charge : Rs.{fixed_charge:.2f}")
    print("----------------------------------------------")
    print(f"Net Bill Amount : Rs.{net_bill:.2f}")
    print("==============================================")
