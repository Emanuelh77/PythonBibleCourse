students = {
    'male': ['Tom', 'Charlie', 'Harry', 'Frank'],
    'female': ['Sarah', 'Jen', 'Sam', 'Emily', 'Emma']
    }

for key in students.keys():
    for name in students[key]:
        if 'a' in name:
            print(name)
