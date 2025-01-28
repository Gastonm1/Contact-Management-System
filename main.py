people = []

## Add Function
def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    
    person = {"name": name,"age": age,"email": email}
    return person

## Delete Function
def delete_contact(people):
    for i, person in enumerate(people): # enumerate give syou the index as well as the element for every single element inside of your list
        print(i + 1,":", person["name"], "|", person["age"], "|", person["email"])

    while True:
        print("Contact list size:", len(people))
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except:
            print("Invalid number")


    people.pop(number - 1)
    print("Person deleted")

print("Hi, welcome to the Contact Management System")
print()

people = []

while True:
    command = input("You can 'Add', 'Delete', or 'Search' and 'Q' for quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print('Person added!')
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        pass
    elif command == "q":
        break
    else:
        print("Invalid command.")

print(person)