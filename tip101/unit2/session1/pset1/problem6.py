def calculate_gpa(report_card):
    gpa = 0
    test = {}
    for i in range(len(report_card)):
        if list(report_card.values())[i] == "A":
            test[list(report_card)[i]] = 4
        elif list(report_card.values())[i] == "B":
            test[list(report_card)[i]] = 3
        elif list(report_card.values())[i] == "C":
            test[list(report_card)[i]] = 2
        elif list(report_card.values())[i] == "D":
            test[list(report_card)[i]] = 1
        else:
            test[list(report_card)[x]] = 0
    for x in range(len(report_card)):
        gpa = gpa + list(test.values())[x]
    gpa = gpa / len(report_card)
    return gpa
report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))