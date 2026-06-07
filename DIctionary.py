print ("Dictionary. it is a collection of key-value pairs")
#For single value
students={
    "name ": "Santosh",
    "marks ": 90,
    "roll no ": 24
}
print(students)
print(students["name "])
#for update value
students["marks"]=95
print(students)
# for add anoter field
students["grade"]="A"
print(students)
# fo cheack field is present or not
print ("name "in students)
print ("age "in students)
# for delete field
del students["roll no "]
print(students)
# for keays and values
print(students.keys())
print(students.values())
# for multiple Dictionary
students=[

    { 
        "name": "Sholok",
        "marks": 90,
        "roll no": 24
    },
    {
        "name": "Rahul",
        "marks": 85,
        "roll no": 25
    },
    {
        "name": "Priya",
        "marks": 92,
        "roll no": 26
    }

]
#accessing information
print(students[0]["name"])
print(students[1]["marks"])
for student in students:
    print(student["name"], student["marks"])