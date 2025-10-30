def calculate_tip(bill,service_quality):
    if service_quality == "poor":
        return bill * .10
    elif service_quality == "average":
        return bill * .15
    elif service_quality == "excellent":
        return bill * .20
    elif service_quality != "poor" or "average" or "excellent":
        return None

tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)