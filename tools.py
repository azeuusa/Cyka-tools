from decoder import run_decoder
from hash import run_hash
from iptracking import run_ip_tracker

def main_menu():
    while True:
        print("""                                                         
 ▄▄▄▄▄▄▄                                        ▄▄       
███▀▀▀▀▀       ▄▄              ██               ██       
███      ██ ██ ██ ▄█▀  ▀▀█▄   ▀██▀▀ ▄███▄ ▄███▄ ██ ▄█▀▀▀ 
███      ██▄██ ████   ▄█▀██    ██   ██ ██ ██ ██ ██ ▀███▄ 
▀███████  ▀██▀ ██ ▀█▄ ▀█▄██    ██   ▀███▀ ▀███▀ ██ ▄▄▄█▀ 
           ██                                            
         ▀▀▀                                             

                                                          
   === Main Menu ===
1. Blyat Decoder
2. Hash Generator
3. IP Tracker
4. Exit
""")
        choice = input("Select an option (1-4): ")
        if choice == '1':
            run_decoder()
        elif choice == '2':
            run_hash()    
        elif choice == '3':
            run_ip_tracker()
        elif choice == '4' or choice.lower() == 'exit':
            print("Exiting. Stay strong, blyat!")
            exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()