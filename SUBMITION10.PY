1.
person = {"name": "Eyouel", "age": 20}
person.clear()
print(person)

2.
student = {"name": "Eyouel", "grade": "A"}
copy_student = student.copy()
print(copy_student)

3.
keys = ["name", "age", "gender"]
new_dict = dict.fromkeys(keys)
print(new_dict)

4.
person = {"name": "Eyouel", "age": 20}
print(person.get("name"))