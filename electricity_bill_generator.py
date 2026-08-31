print(&quot;========== ELECTRICITY BILL GENERATOR ==========&quot;)
consumer_name = input(&quot;Enter Consumer Name: &quot;)
consumer_id = input(&quot;Enter Consumer ID: &quot;)
previous_reading = float(input(&quot;Enter Previous Meter Reading (kWh): &quot;))
current_reading = float(input(&quot;Enter Current Meter Reading (kWh): &quot;))
cost_per_unit = float(input(&quot;Enter Cost per Unit (₹): &quot;))
units = current_reading - previous_reading
energy_charge = units * cost_per_unit
electricity_duty = energy_charge * 0.05
fixed_charge = 100
net_bill = energy_charge + electricity_duty + fixed_charge

print(&quot;\n============== ELECTRICITY BILL ==============&quot;)
print(f&quot;Consumer Name : {consumer_name}&quot;)
print(f&quot;Consumer ID : {consumer_id}&quot;)
print(f&quot;Units Consumed : {units:.2f} kWh&quot;)
print(f&quot;Energy Charge : ₹{energy_charge:.2f}&quot;)
print(f&quot;Electricity Duty(5%) : ₹{electricity_duty:.2f}&quot;)
print(f&quot;Fixed Meter Charge : ₹{fixed_charge:.2f}&quot;)
print(&quot;----------------------------------------------&quot;)
print(f&quot;Net Bill Amount : ₹{net_bill:.2f}&quot;)
print(&quot;==============================================&quot;)
