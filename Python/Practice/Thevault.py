def menu():
    print("\n--- SECURE VAULT ---")
    print("1. Add Password")
    print("2. Get Password")
    print("3. Exit")

passwords = {} # This dictionary stores your data

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == '1':
        service = input("Enter service name (e.g., Email): ")
        pw = input("Enter password: ")
        passwords[service] = pw
        print(f"Password for {service} saved!")
    
    elif choice == '2':
        service = input("Enter service to retrieve: ")
        # .get() prevents crashing if the key doesn't exist
        print(f"Password: {passwords.get(service, 'Not found')}")
    
    elif choice == '3':
        print("Locking Vault...")
        break
        
    else:
        print("Invalid command.")
