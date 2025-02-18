import subprocess
from PIL import Image
import pytesseract
from time import sleep
import json
from handle import handle
import threading
from functools import partial

import json,os
import datetime
import base64

version = 'REGCLONE12.0'



class ldplayer:
    def __init__(self) -> None:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.image_path = 'image/ldplayer_screenshot.png'

        with open('setting_active.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.activemail = config_data["activemail"]
        with open('MACHINE.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.MACHINE = config_data["MACHINE"]
        with open('setting_reg.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.tab_ldplayer = config_data["tab_ldplayer"]
            self.solanreg = config_data["solanreg"]
        with open('setting_ld.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.ADB = config_data[r"pathldplayer"]

    def tenn(self):
        handle().ten()
        with open('ten.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.ten = config_data[r"ten"]
        return self.ten
    def hoo(self):
        handle().name()
        
        with open('ho.json', 'r') as configfile:
            config_data = json.load(configfile)
            self.ho = config_data[r"ho"]

        return self.ho
    
    def adb_command(self,command):
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    
    def is_app_installed(self):
        try:
            command = fr'{self.ADB}\\adb.exe -s {self.DEVICE()[self.j]} shell pm list packages com.facebook.katana'
            result = self.adb_command(command)
            return 'com.facebook.katana' in result.stdout
        except :
            return False
    def install_facebook(self):
        apk_path = 'com.facebook.katana.apk'
        command = fr'{self.ADB}\\adb.exe -s {self.DEVICE()[self.j]} install {apk_path}'
        self.adb_command(command)
    
    def openfb(self):
        if self.is_app_installed():
            self.cachefacebook()
            command = fr'{self.ADB}\\adb.exe -s {self.DEVICE()[self.j]} shell am start -n com.facebook.katana/.LoginActivity'
            self.adb_command(command)
        else:
            print('shjinsad')
            self.install_facebook()
            self.cachefacebook()
            command = fr'{self.ADB}\\adb.exe -s {self.DEVICE()[self.j]} shell am start -n com.facebook.katana/.LoginActivity'
            self.adb_command(command)
    
    def capture_ldplayer_screen(self):
        filename=f'image/ldplayer_screenshot{self.j}.png'
        subprocess.run([fr'{self.ADB}\\adb.exe', '-s', self.DEVICE()[self.j], 'exec-out', 'screencap', '-p'], stdout=open(filename, 'wb'))

    def input(self,text):
        command = fr'{self.ADB}\\adb.exe -s {self.DEVICE()[self.j]} shell input text {text}'
        self.adb_command(command)
        sleep(2)

    def click(self,x,y):
        command = fr'{self.ADB}\\adb.exe -s {self.DEVICE()[self.j]} shell input tap {x} {y}'
        self.adb_command(command)
        sleep(2)

    def cachefacebook(self):
        command = fr'{self.ADB}\\adb.exe -s {self.DEVICE()[self.j]} shell pm clear com.facebook.katana'
        self.adb_command(command)


    def check_page(self):
        
        check = []
        self.image_path = f'image/ldplayer_screenshot{self.j}.png'
        self.capture_ldplayer_screen()
        # Đọc ảnh
        text = pytesseract.image_to_string(Image.open(self.image_path))
        text_list = text.split('\n')
        for idx, line in enumerate(text_list):
            check.append(line)

        return check
    
    def close(self,vm_id):
        command = [fr"{self.ADB}\ldconsole.exe", 'quit', '--name', vm_id]
        self.adb_command(command)

    def setting_LDPlayer(self):
        handle().LDPlayer()

    def DEVICE(self):
        proc = subprocess.Popen(fr"{self.ADB}\adb.exe devices", shell= True, stdout=subprocess.PIPE)
        print(proc)
        serviceList = proc.communicate()[0].decode('ascii').split('\n')

        self.list_device = []
        for i in range(1, len(serviceList)-2):
            try:
                device = serviceList[i].split('\t')[0]
                print(device)
                self.list_device.append(device)
            except:
                pass
        print(self.list_device)
        return self.list_device
    

        

    def open_ldplayer(self,vm_id):
        print(vm_id)
        print(self.j)
        subprocess.run([fr"{self.ADB}\ldconsole.exe", 'launch', '--name', vm_id], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        while True:
            print(1)
            try:
                if len(self.DEVICE()) > int(self.tab_ldplayer)-1:
                    print(self.DEVICE())
                    break
                else:
                    sleep(10)
            except:
                sleep(5)
        device = self.DEVICE()[self.j]
        print(device)
        while True:
            print(2)
            command = fr'{self.ADB}\\adb.exe -s {device} shell dumpsys window windows | findstr mCurrentFocus'
            output = self.adb_command(command)
            print(output[0])
            # Kiểm tra xem giao diện chính của LDPlayer có đang chạy không
            if 'com.ldmnq.launcher3/com.android.launcher3.Launcher' in output[0]:
                break
            else:
                sleep(5)
    def setproxy(self):
        proxy = handle().proxy()
        ip = proxy[0]
        port = proxy[1]
        command_host = fr'{self.ADB}\\adb.exe -s {self.DEVICE()[self.j]} shell settings put global http_proxy {ip}:{port}'
        self.adb_command(command_host)

    def clearproxy(self):
        command_clear_http_proxy = fr'{self.ADB}\\adb.exe -s {self.DEVICE()[self.j]} shell settings put global http_proxy :0'
        self.adb_command(command_clear_http_proxy)
    def maint(self,vm_id,i):
        try:
            
            self.j = i
            self.setting_LDPlayer()
            self.open_ldplayer(vm_id)
            self.openfb()
            for i in range(120):
                if 'Mat khau' in self.check_page() or 'Password' in self.check_page() :
                    self.click(159,579)
                    break
                else:
                    sleep(1)
            for i in range(120):
                if 'Tham gia Facebook' in self.check_page() or 'Join Facebook' in self.check_page():
                    self.click(183,516)
                    break
                else:
                    sleep(1)
            sleep(3)
            self.click(274,482)
            self.click(274,482)
            for i in range(120):
                if 'Tiép tuc voi' in self.check_page() or 'Continue with' in self.check_page():
                    self.click(189,430)
                    break
                elif 'Ban tén gi?'in self.check_page() or "What's your name?" in self.check_page():
                    break
                else:
                    sleep(1)


            self.click(82,274)
            self.input(self.tenn())
            self.click(213,274)
            self.input(self.hoo())
            
            self.click(185,406)
            #--------------------Birthday---------------------------

            self.click(82,362)
            self.input(handle().day())
            self.click(177,367)
            self.input(handle().month())
            self.click(280,367)
            self.input(handle().old())
            self.click(177,367)

            self.click(178,553)
            
            #--------------------gioi tinh---------------------------

            # self.click(190,310)
            self.click(200,388)

            self.click(182,603)
            sleep(2)
            if self.activemail['tempmail']['active'] == 1:
                self.mail = []
                self.mail.append(handle().active())
                #--------------------Number---------------------------

                # self.click(154,315)
                # self.input('0916733227')

                # self.click(177,423)
                # sleep(5)
                #--------------------Email---------------------------

                self.click(172,624)
                self.click(168,313)
                self.input(self.mail[0])

                self.click(172,399)
                sleep(2)
            

            #--------------------Password---------------------------

            self.click(171,269)
            self.pas = []
            self.pas.append(handle().password())
            self.input(self.pas[0])

            self.click(166,393)
            sleep(2)

            #--------------------DieuKhoan---------------------------

            self.click(179,334)
            sleep(2)

            #--------------------Save---------------------------
            for i in range(300):
                if 'LUC KHAC' in self.check_page() or 'NOT NOW' in self.check_page():
                    self.click(214,471)
                    sleep(2)
                    for i in range(300):
                        if 'Email' in self.check_page() or 'Email' in self.check_page():
                            self.click(214,471)
                            break
                        else:
                            sleep(1)
                    print(self.mail,self.pas)

                    #--------------------CODE---------------------------

                    command = fr'{self.ADB}\\adb.exe -s {self.DEVICE()[self.j]} shell input keyevent 4'
                    self.adb_command(command)
                    self.click(150,338)
                    self.click(150,338)
                    self.input(handle().code(self.mail[0]))
                    self.click(180,432)
                    
                    #--------------------LucKhac---------------------------
                    for i in range(120):
                        if 'Luc khac OK' in self.check_page() :
                            sleep(5)
                            f = open(r'facebook.txt','a')
                            f.write(f'{self.mail[0]} {self.pas[0]}\n')
                            f.close()
                            self.close(vm_id)
                            
                            print(self.mail,self.pas)
                            break
                        else:
                            sleep(1)
                    self.close(vm_id)
                elif 'The action attempted has'in self.check_page():
                    print('clone die')
                    self.close(vm_id)
                elif 'Tai théng tin cua ban xu6ng'in self.check_page():
                    print('clone die')
                    self.close(vm_id)
                elif 'Su cé tai'in self.check_page():
                    print('clone die')
                    self.close(vm_id)
                elif 'THU LAI'in self.check_page():
                    print('clone die')
                    self.close(vm_id)   
                elif 'DONG'in self.check_page():
                    print('clone die')
                    self.close(vm_id) 
                elif 'Mat két néi'in self.check_page():
                    print('clone die')
                    self.close(vm_id) 
                else:
                    sleep(1)

            #--------------------Email---------------------------

            
        except:
            print('shinsaddeptrai')
            self.close(vm_id)
def thread():
    with open('MACHINE.json', 'r') as configfile:
        config_data = json.load(configfile)
        MACHINE = config_data["MACHINE"]
    with open('setting_reg.json', 'r') as configfile:
        config_data = json.load(configfile)
        tab_ldplayer = config_data["tab_ldplayer"]
        solanreg = config_data["solanreg"]


    handle().LDPlayer()
    for i in range(0, int(solanreg), int(tab_ldplayer)):

        for j in range(int(tab_ldplayer)):
            while True:
                print(1)
                if len(ldplayer().DEVICE()) == 0:
                    break
                else:sleep(5)
            threads = []
            if i + j < int(solanreg):
                thread =threading.Thread(target=partial(ldplayer().maint, MACHINE[j]["value"], j))
                threads.append(thread)
                thread.start()
        
        # Chờ tất cả các luồng trong batch này hoàn thành
        for thread in threads:
            thread.join()

      
# try:
#     with open('key.json', 'r') as configfile:
#             config_data = json.load(configfile)
#             key = config_data["key"]
# except:
#     key = input('Input Key: ')

#     config_data = {
#             'key': key,
#         }

#     with open('key.json', 'w',encoding='utf-8') as configfile:
#         json.dump(config_data, configfile, indent=4)

# print(f"Generated Key: {key}")
# def validate_key(encoded_key):
#     try:
#         key_bytes = base64.urlsafe_b64decode(encoded_key.encode('utf-8'))
#         key_json = key_bytes.decode('utf-8')
#         key_data = json.loads(key_json)
        
#         expiry_time = datetime.datetime.fromisoformat(key_data['expires_at'])
#         current_time = datetime.datetime.now()
        
#         if current_time < expiry_time and key_data['version'] == version:
#             thread()
#             return True, f"Key is valid until {expiry_time} with version {key_data['version']}"
#         elif key_data['version'] != version:
#             os.remove('key.json')
#             return False, "Version mismatch"
#         else:
#             os.remove('key.json')
#             return False, "Key has expired"
#     except Exception as e:
#         os.remove('key.json')
#         return False, f"Invalid key: {str(e)}"

# is_valid, message = validate_key(key)
# print(f"Validation Result: {message}")