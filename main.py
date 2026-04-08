import os
import sys

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        clear_screen()

        print("=" * 60)
        print("        Wi-Fi Security Analyzer (Launcher)")
        print("=" * 60)

        print("1. Run CLI Version")
        print("2. Run Desktop GUI (Tkinter)")
        print("3. Run Web App (Flask)")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        try:
            if choice == "1":
                print("\nLaunching CLI version...\n")
                os.system("python cli_app.py")
                input("\nPress Enter to return to menu...")

            elif choice == "2":
                print("\nLaunching GUI...\n")
                os.system("python gui_app/gui.py")

            elif choice == "3":
                print("\nLaunching Web App...\n")
                os.system("python web_app/app.py")

            elif choice == "0":
                print("\nExiting program... 👋")
                sys.exit()

            else:
                print("❌ Invalid choice! Try again.")
                input("Press Enter...")

        except Exception as e:
            print(f"\n⚠ Error occurred: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
