import subprocess

def get_wifi_profiles():
    try:
        meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
        data = meta_data.decode('utf-8', errors="backslashreplace").split('\n')
        profiles = []

        for line in data:
            if "All User Profile" in line:
                parts = line.split(":")
                wifi_profile = parts[1].strip()[1:-1]
                profiles.append(wifi_profile)

        return profiles

    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve Wi-Fi profiles.")
        return []

def get_password(profile_name):
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear'])
        results = results.decode('utf-8', errors="backslashreplace").split('\n')
        password = [line.split(":")[1].strip()[1:-1] for line in results if "Key Content" in line]

        return password[0] if password else ""

    except subprocess.CalledProcessError:
        print(f"Error: Unable to retrieve password for {profile_name}.")
        return ""

def main():
    print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
    print("-" * 45)

    profiles = get_wifi_profiles()

    for profile in profiles:
        password = get_password(profile)
        print("{:<30}| {:<}".format(profile, password))

if __name__ == "__main__":
    main()
