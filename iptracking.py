import requests
import webbrowser

def run_ip_tracker():
    while True:
        print("\n=== IP Tracker ===")
        print("1. Track IP")
        print("2. Back")
        choice = input("Select an option (1-2): ")
        if choice == '2' or choice.lower() == 'back':
            return
            
        ip_target = input("Enter target IP: ")
        
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }

        try:
            res = requests.get(f"https://ipapi.co/{ip_target}/json/", headers=headers)
            
            if res.status_code != 200:
                print(f"⚠️ Website blocked us! Status Code: {res.status_code}")
                print("Try to change your VPN server or wait a few minutes.")
                continue

            data = res.json()

            if data.get('error'):
                print(f"Failed: {data.get('reason')}")
                continue

            print("\n" + "="*45)
            print(f"🌐 ADVANCED IP INTELLIGENCE: {ip_target}")
            print("="*45)
            
            print(f"\n[+] GEOGRAPHIC INFORMATION")
            print(f"    - Country/Code : {data.get('country_name')} ({data.get('country_code')})")
            print(f"    - Region/State : {data.get('region')}")
            print(f"    - City/Postal  : {data.get('city')} ({data.get('postal')})")
            print(f"    - Coordinates  : {data.get('latitude')}, {data.get('longitude')}")
            
            print(f"\n[+] NETWORK & SERVICE")
            print(f"    - ASN/Org      : {data.get('asn')} / {data.get('org')}")
            print(f"    - ISP Provider : {data.get('network')}")
            
            print(f"\n[+] REGIONAL DETAILS")
            print(f"    - Timezone     : {data.get('timezone')}")
            print(f"    - Currency     : {data.get('currency_name')} ({data.get('currency')})")
            print(f"    - Country TLD  : {data.get('country_tld')}")
            print(f"    - Calling Code : +{data.get('country_calling_code')}")
            print(f"    - Languages    : {data.get('languages')}")

            print("\n" + "="*45)
            
            coords = f"{data.get('latitude')},{data.get('longitude')}"
            map_choice = input("\n[?] Open exact location in Google Maps? (y/n): ")
            if map_choice.lower() == 'y':
                webbrowser.open(f"https://www.google.com/maps?q={coords}")

        except requests.exceptions.JSONDecodeError:
            print("❌ Error: The website returned HTML instead of JSON (Probably a Bot Challenge/Captcha).")
        except Exception as e:
            print(f"Critical Error: {e}")
            
        input("Press Enter to continue...")

if __name__ == "__main__":
    run_ip_tracker()