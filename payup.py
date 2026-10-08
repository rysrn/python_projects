
#display values
#event_name ="picnic"
#cost = 4000
#service_charge = 275
#group_size = 5
#grand_total = 4275
#total_per_person = 855

#gather input from users
event_name = input("What is the occasion? ")
cost = float(input("How much was spent? "))
service_charge = int(input("Was there a service charge? If yes, how much?  eg 20 for 20%: ").strip("%"))
group_size = int(input("What is the group size? "))

service_charge = float(cost * (service_charge / 100))
grand_total = cost + service_charge
total_per_person = grand_total / group_size

print("Welcome to PayUp!")
print()
print(f"Here's the breakdown for the {event_name}:")
print()
print(f"Cost:  $ {cost: .2f}")
print(f"Service charges:  $ {service_charge: .2f}")
print(f"Group size: {group_size}")
print(f"Grand total: $ {grand_total: .2f}")
print()
print(f"Each person must PayUp: $ {total_per_person: .2f}")
