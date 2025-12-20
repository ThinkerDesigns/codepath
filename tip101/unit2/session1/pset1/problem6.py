# WIP - need to find out how to make the string of ABCDF into seperate ints
def calculate_gpa(report_card):
    gpa = 0
    for x in range(len(report_card)):
        gpa = gpa + list(report_card)[x]
    gpa = gpa / len(report_card)
    return gpa
report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))