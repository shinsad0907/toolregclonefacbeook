import subprocess
import random
import os
import shutil

# Constants
CHROMIUM_EXE = r"C:\Users\Shin\AppData\Local\Chromium\Application\chrome.exe"
BASE_PROFILE_DIR = r"C:\shin\shinsad\chromium_profiles"
PROXY_SERVERS = [
    "hndc63.proxy3g.com:24300",
    "hndc64.proxy3g.com:24301",
    "hndc65.proxy3g.com:24302"
]

# Device Profiles for better emulation
DEVICES = [
    {
        "name": "iPhone 14 Pro",
        "model": "A3494",
        "ios_version": "16.0",
        "width": 430,
        "height": 932,
        "safari_version": "16.0",
        "build_id": "20V372"
    },
]

def get_random_device():
    return random.choice(DEVICES)

def get_random_proxy():
    return random.choice(PROXY_SERVERS)

def generate_user_agent(device):
    if 'ios_version' in device:
        return (f"Mozilla/5.0 (iPhone; CPU iPhone OS {device['ios_version'].replace('.', '_')} like Mac OS X) "
                f"AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{device['safari_version']} "
                f"Mobile/{device['build_id']} Safari/604.1")
    else:
        return (f"Mozilla/5.0 (Linux; Android {device['android_version']}; {device['model']}) "
                f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{device['chrome_version']} Mobile Safari/537.36")

def setup_profile_directory():
    os.makedirs(BASE_PROFILE_DIR, exist_ok=True)
    profile_id = random.randint(1000, 9999)
    profile_dir = os.path.join(BASE_PROFILE_DIR, f"profile_{profile_id}")

    if os.path.exists(profile_dir):
        shutil.rmtree(profile_dir)
    os.makedirs(profile_dir)
    return profile_dir

def launch_chromium():
    device = get_random_device()
    proxy = get_random_proxy()
    profile_dir = setup_profile_directory()
    user_agent = generate_user_agent(device)
    ip = input("Enter IP: ")
    port = input("Enter Port: ")
    print(f"Launching with device: {device['name']}")
    print(f"User Agent: {user_agent}")
    print(f"Using Proxy: {proxy}")

    cmd = [
        CHROMIUM_EXE,
        f"--user-data-dir={profile_dir}",
        f"--window-size={device['width']},{device['height']}",
        f"--user-agent={user_agent}",
        f"--proxy-server={ip}:{port}",
        "--disable-blink-features=AutomationControlled",
        "--disable-extensions",
        "--disable-popup-blocking",
        "--disable-infobars",
        "--no-default-browser-check",
        "--disable-component-update",
        "--enable-features=TouchEvents,NetworkService",
        "--disable-features=IsolateOrigins,site-per-process",
        "--disable-web-security",
        "--ignore-certificate-errors",
        "--disable-permissions-api",
        "--force-device-scale-factor=1",
        "--disable-gpu",
        "--hide-scrollbars",
        "--metrics-recording-only",
        "--mute-audio",
        "--no-sandbox",
        "https://m.facebook.com"
    ]

    subprocess.Popen(cmd)

def main():
    launch_chromium()

if __name__ == "__main__":
    main()
