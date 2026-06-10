student={}

student["name"]=input("Enter your name: ")
student["programming"]=int(input("Programming skills: (1-10):"))
student["design"]=int(input("UI design skills: (1-10): "))
student["networking"]=int(input("Networking skills: (1-10): "))

#determinate career path (cpndition)
if student["programming"]>student["design"] and student["programming"]>student["networking"]:
    student["career_path"]="Software Developer"
elif student["design"]>student["programming"] and student["design"]>student["networking"]:
    student["career_path"]="UI/UX Designer"
elif student["networking"]>student["programming"] and student["networking"]>student["design"]:
    student["career_path"]="Network Engineer"
elif student["programming"]==student["design"] and student["programming"]>student["networking"]:
    student["career_path"]="Software Developer/UI/UX Designer"
elif student["programming"]==student["networking"] and student["programming"]>student["design"]:
    student["career_path"]="Software Developer/Network Engineer"
elif student["design"]==student["networking"] and student["design"]>student["programming"]:
    student["career_path"]="UI/UX Designer/Network Engineer"
elif student["programming"]==student["design"] and student["programming"]==student["networking"]:
    student["career_path"]="Software Developer/UI/UX Designer/Network Engineer"
#prints
print(f"Name: {student['name']}")
print(f"Programming: {student['programming']}")
print(f"Design: {student['design']}")
print(f"Networking: {student['networking']}")
print(f"Career Path: {student['career_path']}")
