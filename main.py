import getpass
import os
import random
import string
import time
from datetime import datetime, timedelta

import colorama
logged_in = False


def simulate_network_scanning(radius):
    try:
        print(f"Initiating network scanning within a radius of {radius} meters...")
        time.sleep(2)  # Simulate scanning process
        print("Scanning complete.")
        print("Found the following IP addresses:")
        ip_addresses = generate_random_ip_addresses(50)
        for ip in ip_addresses:
            print(ip)
    except Exception as e:
        print(f"An error occurred during network scanning: {str(e)}")


def simulate_password_cracking():
    try:
        ip_address = input("Enter the IP address to crack the password: ")
        payload = input("Enter the payload: ")
        print(f"Cracking password for IP address: {ip_address} with payload: {payload}")
        time.sleep(2)  # Simulate password cracking process
        print("Password cracked successfully.")
        directory = generate_random_files()
        print("Found the following files:")
        for i, file in enumerate(directory, start=1):
            print(f"{i}. {file}")
        file_choice = input("Enter the number of the file to use: ")
        selected_file = directory[int(file_choice) - 1]
        print(f"Using file: {selected_file}")
        time.sleep(2)  # Simulate using the selected file
        print("Process completed.")
    except (ValueError, IndexError) as e:
        print("Invalid input. Please try again.")
    except Exception as e:
        print(f"An error occurred during password cracking: {str(e)}")


def simulate_john_the_ripper():
    try:
        print("Initializing John the Ripper...")
        time.sleep(2)  # Simulate John the Ripper initialization
        print("John the Ripper initialized.")
        hash_file = input("Enter the path to the hash file: ")
        wordlist = input("Enter the path to the wordlist file: ")
        print(f"Cracking passwords using hash file: {hash_file} and wordlist: {wordlist}")
        time.sleep(2)  # Simulate password cracking process
        print("Passwords cracked successfully.")
        print("Found the following passwords:")
        passwords = generate_random_passwords(10)
        for password in passwords:
            print(password)
        print("Process completed.")
    except Exception as e:
        print(f"An error occurred during John the Ripper: {str(e)}")


def simulate_distributed_denial_of_service():
    try:
        ip_address = input("Enter the target IP address: ")
        duration = int(input("Enter the duration of the attack (in seconds): "))
        print(f"Initiating distributed denial of service attack on IP address: {ip_address} for {duration} seconds...")
        time.sleep(duration)  # Simulate attack duration
        print("Attack completed.")
    except (ValueError, TypeError) as e:
        print("Invalid input. Please enter a valid IP address and duration.")
    except Exception as e:
        print(f"An error occurred during distributed denial of service: {str(e)}")


def simulate_data_exfiltration():
    try:
        file_path = input("Enter the path of the file to exfiltrate: ")
        destination_ip = input("Enter the destination IP address: ")
        print(f"Exfiltrating file: {file_path} to destination IP address: {destination_ip}")
        time.sleep(2)  # Simulate data exfiltration process
        print("Data exfiltration complete.")
        print("Process completed.")
    except Exception as e:
        print(f"An error occurred during data exfiltration: {str(e)}")


def simulate_system_bypass():
    try:
        print("Bypassing system security...")
        time.sleep(2)  # Simulate system bypass process
        print("System security bypassed.")
        print("Process completed.")
    except Exception as e:
        print(f"An error occurred during system bypass: {str(e)}")


def simulate_phone_tracking():
    try:
        phone_number = input("Enter the phone number to track: ")
        print(f"Tracking phone number: {phone_number}")
        time.sleep(2)  # Simulate phone tracking process
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        print(f"Phone location found - Latitude: {latitude}, Longitude: {longitude}")
        print("Process completed.")
    except Exception as e:
        print(f"An error occurred during phone tracking: {str(e)}")


def simulate_security_camera_hacking():
    try:
        ip_address = input("Enter the IP address of the security camera: ")
        print(f"Hacking into security camera with IP address: {ip_address}")
        time.sleep(2)  # Simulate security camera hacking process
        print("Security camera hacked successfully.")
        print("Accessing camera feed...")
        time.sleep(2)  # Simulate accessing camera feed
        print("Camera feed accessed.")
        print("Process completed.")
    except Exception as e:
        print(f"An error occurred during security camera hacking: {str(e)}")


def simulate_oracle_operations():
    try:
        print("Initiating Oracle operations...")
        time.sleep(2)  # Simulate Oracle operations initialization
        print("Oracle operations initiated.")
        target_name = input("Enter the name of the target: ")
        print(f"Searching for case files starting with: {target_name}")
        time.sleep(2)  # Simulate searching process
        case_files = search_case_files(target_name)
        selected_file = None  # Initialize selected_file variable

        while True:
            print("Found the following case files:")
            for i, case_file in enumerate(case_files, start=1):
                print(f"{i}. {case_file}")

            file_choice = input("Enter the number of the file to investigate or press Enter to exit: ")
            if not file_choice:
                break

            try:
                selected_index = int(file_choice) - 1
                if 0 <= selected_index < len(case_files):
                    selected_file = case_files[selected_index]
                    print(f"Selected file: {selected_file}")
                    confirmation = input("Is this the correct file? (y/n): ")

                    if confirmation.lower() == "y":
                        print("Cross-referencing case files through the Police Database...")
                        time.sleep(2)  # Simulate connection initialization
                        print("Connecting to Oracle...")
                        time.sleep(2)  # Simulate connection establishment
                        print("Searching database...")
                        progress_bar(1, 100)  # Simulate search progress
                        print("Search complete.")
                        print("Output displayed on Screen 7.")
                        time.sleep(3)  # Delay for 3 seconds

                        # Create CASEFILES folder on the desktop if it doesn't exist
                        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
                        casefiles_folder = os.path.join(desktop_path, "CASEFILES")
                        if not os.path.exists(casefiles_folder):
                            os.makedirs(casefiles_folder)

                        # Create a text file with the selected file name in CASEFILES folder
                        file_path = os.path.join(casefiles_folder, selected_file)
                        with open(file_path, "w") as file:
                            file.write("This is the content of the file.")

                        # Open the file on the screen
                        os.system(f"open {file_path}")
                        print("File opened on Screen 7.")

                        break

                else:
                    print("Invalid file number. Please try again.")

            except ValueError:
                print("Invalid input. Please enter a valid file number.")

        if selected_file and selected_file not in case_files:
            case_files.append(selected_file)  # Add the selected file back to the list

    except Exception as e:
        print(f"An error occurred during Oracle operations: {str(e)}")


def progress_bar(start, end):
    total_time = 10  # Total time for the progress bar (in seconds)
    step_time = total_time / (end - start + 1)
    elapsed_time = 0

    for i in range(start, end + 1):
        print(f"Progress: {i}/{end} [{'#' * i + '-' * (end - i)}] {elapsed_time}/{total_time} seconds", end="\r",
              flush=True)
        time.sleep(step_time)
        elapsed_time += step_time

    print()  # Print a newline to ensure the next line is displayed properly


def search_case_files(target_name, exclude=None):
    num_files = random.randint(1, 107)
    case_files = []
    for _ in range(num_files):
        file_name = generate_random_file_name(target_name)
        case_files.append(file_name)
    return case_files


def generate_random_file_name(target_name):
    current_date = datetime.now()
    start_date = datetime(2013, 6, 1)
    random_date = start_date + timedelta(days=random.randint(0, (current_date - start_date).days))
    username = random.choice(["Prophet", "Beetle", "Spartan"])
    return f"{target_name}_{random_date.strftime('%Y%m%d')}_{username}.txt"


def generate_random_ip_addresses(num_addresses):
    ip_addresses = []
    for _ in range(num_addresses):
        ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))
        ip_addresses.append(ip)
    return ip_addresses


def generate_random_files():
    num_files = random.randint(5, 10)
    directory = []
    for _ in range(num_files):
        file_name = generate_random_file_name("target")
        directory.append(file_name)
    return directory


def generate_random_passwords(num_passwords):
    passwords = []
    for _ in range(num_passwords):
        password = generate_random_password()
        passwords.append(password)
    return passwords


def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password_length = random.randint(8, 12)
    password = ''.join(random.choice(characters) for _ in range(password_length))
    return password


def display_welcome_message():
    ascii_art = '''
        *******       *******       ********    **     **   ********  
        /**////**     **/////**     **//////**  /**    /**  /**/////   
        /**   /**    **     //**   **      //   /**    /**  /**        
        /*******    /**      /**  /**           /**    /**  /*******   
        /**///**    /**      /**  /**    *****  /**    /**  /**////    
        /**  //**   //**     **   //**  ////**  /**    /**  /**        
        /**   //**   //*******     //********   //*******   /********  
        //     //     ///////       ////////     ///////    ////////   
    '''

    purple = colorama.Fore.MAGENTA
    reset = colorama.Style.RESET_ALL

    lines = ascii_art.split('\n')
    for line in lines:
        print(purple + line + reset)
        time.sleep(0.1)  # Adjust the delay time as desired

    print(purple + "Welcome! Choose an option to proceed:")
    print("1. Network Scanning")
    print("2. Password Cracking")
    print("3. John the Ripper")
    print("4. Distributed Denial of Service")
    print("5. Data Exfiltration")
    print("6. System Bypass")
    print("7. Phone Tracking")
    print("8. Security Camera Hacking")
    print("9. Oracle Operations")
    print("10. Exit" + reset)


def process_user_choice(choice):
    if choice == "1":
        radius = int(input("Enter the scanning radius (in meters): "))
        simulate_network_scanning(radius)
    elif choice == "2":
        simulate_password_cracking()
    elif choice == "3":
        simulate_john_the_ripper()
    elif choice == "4":
        simulate_distributed_denial_of_service()
    elif choice == "5":
        simulate_data_exfiltration()
    elif choice == "6":
        simulate_system_bypass()
    elif choice == "7":
        simulate_phone_tracking()
    elif choice == "8":
        simulate_security_camera_hacking()
    elif choice == "9":
        simulate_oracle_operations()
    elif choice == "10":
        print("Exiting...")
        time.sleep(1)
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")

    # Add the following line to display the welcome message after every operation
    display_welcome_message()


def login_screen():
    logged_in = False
    # Users and their credentials
    users = {
        "BEETLE": "3536556",
        "SPARTAN": "346567",
        "PROPHET": "952345",
    }

    max_attempts = 3
    attempts = 0


    while attempts < max_attempts and logged_in != True:
        # Capture user input
        print("Enter Credentials.")
        print("-----------------------------")
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        # Check credentials
        if username in users and users[username] == password:
            logged_in = True
            print(f"ACCESS GRANTED - Welcome {username.upper()}")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            display_welcome_message()
        else:
            print("Invalid username or password. Access denied.")
            attempts += 1
    if logged_in != True:
        print("Maximum login attempts reached. Exiting.")
        exit()

def main():
    login_screen()
    while True:
            choice = input("Enter your choice: ")
            process_user_choice(choice)
            print("\n")



if __name__ == "__main__":
    main()
