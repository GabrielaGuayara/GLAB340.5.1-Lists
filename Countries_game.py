import random

countries = ["Ecuador", "Peru", "Venezuela", "Colombia", "Argentina", "Mexico", "Bolivia", "Chile"]

# Create a function to generate a random target list
def generate_target():
    target = random.sample(countries, random.randint(2, 5))
    return target

# Create a function to display the current list and target list to the user
def display_lists(current, target):
    print("Current list:", current)
    print("Target list:", target)

# Create a function to allow the user to perform operations on the list
def countries_list(current):
    print("Choose an operation:")
    print("1. Append a country to the end of the list")
    print("2. Extend the list with another list")
    print("3. Concatenate two elements in the list")
    print("4. Traverse the list and view its elements")
    print("5. Modify an element in the list")
    print("6. Insert an element at a specific index in the list")
    print("7. Pop an element from the list")
    print("8. Remove a specific element from the list")
    print("9. Sort the list in ascending or descending order")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        country = input("Enter a country to append: ")
        current.append(country)
    elif choice == 2:
        other_list = input("Enter a comma-separated list to extend with: ").split(",")
        current.extend(other_list)
    elif choice == 3:
        index1 = int(input("Enter the index of the first element: "))
        index2 = int(input("Enter the index of the second element: "))
        if index1 >= 0 and index1 < len(current) and index2 >= 0 and index2 < len(current):
            current[index1] += current[index2]
            del current[index2]
        else:
            print("Invalid index")
    elif choice == 4:
        print("List elements:")
        for country in current:
            print(country)
    elif choice == 5:
        index = int(input("Enter the index of the element to modify: "))
        if index >= 0 and index < len(current):
            country = input("Enter the new country: ")
            current[index] = country
        else:
            print("Invalid index")
    elif choice == 6:
        index = int(input("Enter the index to insert at: "))
        if index >= 0 and index <= len(current):
            country = input("Enter the new country: ")
            current.insert(index, country)
        else:
            print("Invalid index")
    elif choice == 7:
        if len(current) > 0:
            country = current.pop()
            print("Popped country:", country)
        else:
            print("List is empty")
    elif choice == 8:
        country = input("Enter a country to remove: ")
        if country in current:
            current.remove(country)
        else:
            print("Country not found in list")
    elif choice == 9:
        ascending = input("Sort in ascending order? (y/n) ").lower() == "y"
        current.sort(reverse=not ascending)
    else:
        print("Invalid choice")

    return


countries_list(countries)