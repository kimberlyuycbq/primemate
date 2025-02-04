import os
import subprocess
import ctypes
from datetime import datetime, timedelta

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def block_application(app_path):
    """Block a specific application by modifying the Windows hosts file."""
    if not os.path.exists(app_path):
        print(f"Error: {app_path} does not exist.")
        return

    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    app_name = os.path.basename(app_path)

    with open(hosts_path, 'a') as hosts_file:
        hosts_file.write(f'127.0.0.1 {app_name}\n')

    print(f"{app_name} has been blocked.")

def unblock_application(app_path):
    """Unblock a specific application by modifying the Windows hosts file."""
    if not os.path.exists(app_path):
        print(f"Error: {app_path} does not exist.")
        return

    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    app_name = os.path.basename(app_path)
    new_lines = []

    with open(hosts_path, 'r') as hosts_file:
        lines = hosts_file.readlines()

    for line in lines:
        if app_name not in line:
            new_lines.append(line)

    with open(hosts_path, 'w') as hosts_file:
        hosts_file.writelines(new_lines)

    print(f"{app_name} has been unblocked.")

def main():
    if not is_admin():
        print("Please run this program as an administrator.")
        return

    print("Welcome to PrimeMate - Enhance your privacy by blocking specific applications.")
    while True:
        print("\n1. Block an application")
        print("2. Unblock an application")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            app_path = input("Enter the full path of the application to block: ")
            block_application(app_path)
        elif choice == '2':
            app_path = input("Enter the full path of the application to unblock: ")
            unblock_application(app_path)
        elif choice == '3':
            print("Exiting PrimeMate.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()