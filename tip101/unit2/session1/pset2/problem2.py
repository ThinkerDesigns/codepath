def student_directory(student_names):
    names = {}
    for x in range(len(student_names)):
        if student_names[x] not in names:
            names[x] = student_names[x]
    return names
student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
print(student_directory(student_names))