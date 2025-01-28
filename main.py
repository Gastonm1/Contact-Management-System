people = []

## Add Function
def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    
    person = {"name": name,"age": age,"email": email}
    return person

def display_people(people):
    for i, person in enumerate(people): # enumerate give syou the index as well as the element for every single element inside of your list
        print(i + 1,":", person["name"], "|", person["age"], "|", person["email"])

## Delete Function
def delete_contact(people):
    display_people(people)

    while True:
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

## Basic Search Function
def search_contact(people):
    search_name = input("Search for a name: ").lower()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)
        
    display_people(results)
        



#App Start
print("Hi, welcome to the Contact Management System")
print()

people = [
    {"name": "Tim",
     "age" : 24,
     "email": "tim@nomail.com"
     },
     {"name": "Timothy",
     "age" : 27,
     "email": "timothy@nomail.com"
     },
     {"name": "Joe",
     "age" : 28,
     "email": "joe@nomail.com"
     }
]

while True:
    print()
    print("Contact list size:", len(people))
    command = input("You can 'Add', 'Delete', or 'Search' and 'Q' for quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print('Person added!')
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search_contact(people)
    elif command == "q":
        break
    else:
        print("Invalid command.")

print(person)