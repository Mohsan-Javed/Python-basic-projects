import json
import os

def add_contact(contacts):
    # 1. Gather information from the user
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    
    # 2. Create a dictionary to hold this contact's data
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    # 3. Add the dictionary to our main list
    contacts.append(contact)
    print(f"\nContact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("\nYour contact book is empty.")
        return
        
    print("\n--- Contact List ---\n")
    # We use enumerate to show a number for each contact
    for index, contact in enumerate(contacts, start=1):
        # We access values in the dictionary using their [keys]
        print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact(contacts):
    if not contacts:
        print("\nYour contact book is empty.")
        return
        
    search_name = input("\nEnter the name to search for: ").strip().lower()
    found = False
    
    print(f"\n--- Search Results for '{search_name}' ---")
    for contact in contacts:
        # We use .lower() on both sides to make the search case-insensitive
        if contact['name'].lower() == search_name:
            print(f"Found - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
            
    if not found:
        print("No contact found with that name.")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
        
    search_name = input("\nEnter the contact name to delete: ").strip().lower()
    
    # We loop through the list to find a dictionary with a matching name
    for index, contact in enumerate(contacts):
        if contact['name'].lower() == search_name:
            # Once found, we pop it using the current index
            removed = contacts.pop(index)
            print(f"Contact '{removed['name']}' deleted successfully.")
            return # We exit the function immediately after deleting
            
    # If the loop finishes without returning, it means no match was found
    print("No contact found with that name.")

def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as file:
        # json.dump() turns the Python list of dictionaries into a JSON string
        # indent=4 makes the file look "pretty" and walkable for humans
        json.dump(contacts, file, indent=4)
    print("\nContacts saved to file.")

def load_contacts(filename="contacts.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            # json.load() reads the file and turns it back into a Python list of dictionaries
            return json.load(file)
    return []

def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Book ---\n")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
