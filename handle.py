import json
import subprocess
import random
import string
from datetime import datetime
import requests
class handle:
    def __init__(self) -> None:
        with open('setting_ld.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.pathld = config_data["pathldplayer"]
        with open('setting_reg.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.tab_ldplayer = config_data["tab_ldplayer"]
        with open('Advanced_settings.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.CPU = config_data["CPU"]
            self.RAM = config_data["RAM"]
            self.WIDTH = config_data["WIDTH"]
            self.HEIGHT = config_data["HEIGHT"]
            self.DPI = config_data["DPI"]
            self.ADB = config_data["ADB"]
        with open('setting_account.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.nameaccount = config_data["nameaccount"]
            self.random_password = config_data["random_password"]
            self.passwordd = config_data["password"]
            self.oldmin = config_data["oldmin"]
            self.oldmax = config_data["oldmax"]
            self.sexx = config_data["sex"]
        with open('setting_active.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.activemail = config_data["activemail"]
        with open('setting_ip.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.web = config_data["web_proxy"]
            self.key = config_data["key_proxy"]

        self.cookies = {
            '_ga': 'GA1.2.401332530.1720887237',
            '_gid': 'GA1.2.1981299547.1721019435',
            '__gads': 'ID=2eff6822ca39ca97:T=1720887241:RT=1721042697:S=ALNI_Mbu77KM5OIvbbE41v049D6gNQf5ww',
            '__gpi': 'UID=00000e8fed90a47f:T=1720887241:RT=1721042697:S=ALNI_MbsLGdHd6q28FWCH_H__FU_82H7rg',
            '__eoi': 'ID=c63dee7adcfc2ac5:T=1720887241:RT=1721042697:S=AA-AfjbxaXtk7MQoidJkcSnrLfJT',
            'FCNEC': '%5B%5B%22AKsRol8hL2Ovf3Mhf8kx75Z9qRhebadniOWalFwa70P2rH2fPrztAj3PFSef0ZdpJXO_vHc0xXtwVLOWTXHqHySi6h_d3kwH6H9V7I8IBKTiKIvE_lFXp1cJtXrFUynoKFglo4AOS_YYsosf306lL-jwVsGxjTdS6A%3D%3D%22%5D%5D',
            '_gat': '1',
            '_ga_3DVKZSPS3D': 'GS1.2.1721106026.4.0.1721106031.55.0.0',
        }

        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
            'application-name': 'web',
            'application-version': '2.4.1',
            'content-type': 'application/json;charset=UTF-8',
            # 'cookie': '_ga=GA1.2.401332530.1720887237; _gid=GA1.2.1981299547.1721019435; __gads=ID=2eff6822ca39ca97:T=1720887241:RT=1721042697:S=ALNI_Mbu77KM5OIvbbE41v049D6gNQf5ww; __gpi=UID=00000e8fed90a47f:T=1720887241:RT=1721042697:S=ALNI_MbsLGdHd6q28FWCH_H__FU_82H7rg; __eoi=ID=c63dee7adcfc2ac5:T=1720887241:RT=1721042697:S=AA-AfjbxaXtk7MQoidJkcSnrLfJT; FCNEC=%5B%5B%22AKsRol8hL2Ovf3Mhf8kx75Z9qRhebadniOWalFwa70P2rH2fPrztAj3PFSef0ZdpJXO_vHc0xXtwVLOWTXHqHySi6h_d3kwH6H9V7I8IBKTiKIvE_lFXp1cJtXrFUynoKFglo4AOS_YYsosf306lL-jwVsGxjTdS6A%3D%3D%22%5D%5D; _gat=1; _ga_3DVKZSPS3D=GS1.2.1721106026.4.0.1721106031.55.0.0',
            'origin': 'https://temp-mail.io',
            'priority': 'u=1, i',
            'referer': 'https://temp-mail.io/',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }
    def LDPlayer(self):
        self.save_as_machine()
        self.settingld()

    def get_id_machine(self):
        result = subprocess.run([f'{self.pathld}\ldconsole.exe', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout.strip()
        # Mỗi dòng trong output đại diện cho một máy ảo
        vm_list = output.splitlines()
        if vm_list:
            # Lấy ID của máy ảo đầu tiên (giả sử ID là phần đầu tiên của mỗi dòng)
            return vm_list
    def save_as_machine(self):
        save_machine = []
        for i in range(int(self.tab_ldplayer)):
            save_machine.append({f"value" : self.get_id_machine()[i]})
        print(save_machine)
        config_data = {
            'MACHINE': []
        }
        for setting in save_machine:
            config_data["MACHINE"].append(setting)

        with open('MACHINE.json', 'w',encoding='utf-8') as configfile:
            json.dump(config_data, configfile, indent=4)

    def settingld(self):
        for i in range(int(self.tab_ldplayer)):
            # Đọc tệp JSON cấu hình
            with open(fr'{self.pathld}\vms\config\leidian{i}.config', 'r', encoding='utf-8') as file:
                config = json.load(file)
            # Chỉnh sửa các giá trị CPU, RAM và độ phân giải
            config['advancedSettings.resolution']['width'] = int(self.WIDTH)
            config['advancedSettings.resolution']['height'] = int(self.HEIGHT)
            config['advancedSettings.resolutionDpi'] = int(self.DPI)
            config['advancedSettings.cpuCount'] = int(self.CPU)
            config['advancedSettings.memorySize'] = int(self.RAM)
            config['basicSettings.adbDebug'] = int(self.ADB)

            # Ghi lại tệp JSON cấu hình
            with open(fr'{self.pathld}\vms\config\leidian{i}.config', 'w', encoding='utf-8') as file:
                json.dump(config, file, indent=4, ensure_ascii=False)

    def name(self):
        if self.nameaccount == '1':
            first_names = ["Nguyen", "Tran", "Le", "Pham", "Hoang", "Phan", "Vu", "Vo", "Dang", "Bui", "Do", "Ho"]

        else:
            first_names = [
                    "John", "Jane", "Michael", "Emily", "William", "Sophia", "David", "Olivia",
                    "Liam", "Emma", "Noah", "Ava", "James", "Isabella", "Ethan", "Mia",
                    "Alexander", "Sophia", "Logan", "Olivia", "Lucas", "Amelia", "Jackson", "Ella",
                    "Jack", "Avery", "Benjamin", "Grace", "Henry", "Chloe", "Sebastian", "Lily",
                    "Elijah", "Charlotte", "Caleb", "Abigail", "Gabriel", "Emily", "Mason", "Scarlett",
                    "Dylan", "Madison", "Nathan", "Aria", "Evan", "Riley", "Samuel", "Zoe"
                ]
        config_data = {
                'ho': f'{random.choice(first_names)}',
                }

        with open('ho.json', 'w',encoding='utf-8') as configfile:
            json.dump(config_data, configfile, indent=4)
    def ten(self):
        if self.nameaccount == '1':
            last_names = ["Anh", "Binh", "Chau", "Dung", "Hoa", "Hung", "Khanh", "Lam", "Linh", "Mai", "Minh", "Nam", "Phuong", "Quoc", "Sang", "Son", "Tam", "Thao", "Tuan", "Vy"]
        else:
            last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]
        config_data = {
            'ten': f'{random.choice(last_names)}',
        }

        with open('ten.json', 'w',encoding='utf-8') as configfile:
            json.dump(config_data, configfile, indent=4)
    
    def password(self):
        if self.random_password == '1':
            characters = string.ascii_letters + string.digits
            passwordd = ''.join(random.choice(characters) for i in range(12))
        else:
            passwordd = self.passwordd
        return passwordd
        # print(str(passwordd))


    def sex(self):
        if self.sexx == '1':
            return 200,388
        elif self.sexx == '3':
            random_sex = ['200 388','190 310']
            print(random.choice(random_sex))
            return random.choice(random_sex)
        else:
            return 190,310
    def day(self):
        day = random.randint(1,28)
        return day
    def month(self):
        month = random.randint(1,12)
        return f'thg {month}'
    def old(self):
        oldd = random.randint(int(self.oldmin), int(self.oldmax))
        nam_hien_tai = datetime.now().year
        nam_sinh = nam_hien_tai - oldd
        return nam_sinh
    def proxy(self):
        if self.web == 1:
            pro = requests.get(f'https://proxymxh.com/api/GetNewip.php?api_key={self.key}')
            return pro.json()['data']['ip'], pro.json()['data']['port']
        # requests.get('https://proxyxoay.net/api/rotating-proxy/change-key-ip/cece1d12-92d1-4dbe-8b6e-b0a61d529ca9')
        # getproxy = requests.get('https://proxyxoay.net/api/rotating-proxy/key-status/cece1d12-92d1-4dbe-8b6e-b0a61d529ca9').json()
        # return (getproxy['data']['proxy_connection']['ip'],getproxy['data']['proxy_connection']['http_ipv4'])
    def active(self):
        if self.activemail['tempmail']['active'] == 1:
            json_data = {
            'min_name_length': 10,
            'max_name_length': 10,
            }

            response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new', cookies=self.cookies, headers=self.headers, json=json_data)
            return response.json()["email"]
    def code(self,mail):
        response = requests.get(
            f'https://api.internal.temp-mail.io/api/v3/email/{mail}/messages',
            cookies=self.cookies,
            headers=self.headers,
        )
        return response.json()[0]["subject"].split()[0]
# handle().proxy()

