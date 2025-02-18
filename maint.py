import tkinter as tk
from tkinter import ttk 
from tkinter import font as tkfont
from manager import manager
import threading
import ldplayer
import json,os
import datetime
import base64

version = 'REGCLONE12.0'
class giaodien():
    def __init__(self) -> None:
        self.nameacc = []
        self.tokenacc = []
        super().__init__()
        self.root = tk.Tk()
        self.root.title("Tool Gộp By VoLeTrieuLan")
        self.root.geometry("1350x750")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text='Setting')
        self.notebook.add(self.tab2, text='Account')
    def tab(self):
        self.Setting = tk.Frame(self.tab1,bg='white',highlightbackground='black',
                    highlightthickness=2)
        self.Setting.pack(side=tk.LEFT,fill="both", expand=True)
        self.Setting.pack_propagate(False)
        self.Setting.configure(width = 1350, height = 850  )
        self.Setting.place(x=0,y=0)

        self.accountt = tk.Frame(self.tab2,bg='#2f4f4f',highlightbackground='black',
                    highlightthickness=2)
        self.accountt.pack(side=tk.LEFT)
        self.accountt.pack_propagate(False)
        self.accountt.configure(width = 1350, height = 850  )
        self.accountt.place(x=0,y=0)

        self.account_list()
        self.setting_reg()
        self.setting_LDPlayer()
        self.setting_ip()
        self.setting_account()
        self.setting_active()
        self.interaction()
        self.button()
        self.account()

        self.root.mainloop()
    def account_list(self):
        self.act_list = tk.Frame(self.Setting,highlightbackground='black',
                    highlightthickness=2)
        self.act_list.pack(side=tk.LEFT,fill="both", expand=True)
        self.act_list.pack_propagate(False)
        self.act_list.configure(width = 400, height = 850  )
        self.act_list.place(x=5,y=125)

        scrollbar = tk.Scrollbar(self.act_list, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        style = ttk.Style(self.root)
        style.configure(style="Treeview", height=10)
        self.al = ttk.Treeview(self.act_list, yscrollcommand=scrollbar.set) 
        self.al.configure(style="Treeview", height=50)
        self.al.pack(expand=True, fill="both")
        self.al["columns"] = ("one", "two", "three")
        self.al.column("one", width=70)
        self.al.column("two", width=50)
        self.al.column("three", width=280)

        
        self.al.heading("one", text="Chọn", anchor=tk.W)
        self.al.heading("two", text="STT", anchor=tk.W)
        self.al.heading("three", text="Trạng thái", anchor=tk.W)

        self.al['show'] = 'headings'
    
    def run(self):
        for _ in range(1):
                thread = threading.Thread(target=ldplayer.thread)
                thread.start()

    def setting_reg(self):
        self.sett_reg = tk.Frame(self.Setting,background='white',highlightbackground='black',
                    highlightthickness=2)
        self.sett_reg.pack(side=tk.LEFT,fill="both", expand=True)
        self.sett_reg.pack_propagate(False)
        self.sett_reg.configure(width = 450, height = 90  )
        self.sett_reg.place(x=410,y=30)

        #--------------------------------------------------Cấu Hình Tạo-----------------------------------------------

        self.solanreg= tk.StringVar()
        self.tab_ldplayer =tk.StringVar()
        self.timechootp = tk.StringVar()
        self.doiipsau = tk.StringVar()

        label = tk.Label(self.Setting, text="Cấu Hình Tạo",fg='black',bg='white', font=("Arial", 15, "bold"))
        label.place(x=410,y=15)

        label = tk.Label(self.sett_reg, text="Số lần reg: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=15)
        
        label = tk.Label(self.sett_reg, text="Luồng LDPlayer: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=185,y=15)

        label = tk.Label(self.sett_reg, text="Time chờ OTP: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=45)

        label = tk.Label(self.sett_reg, text="Đổi Ip sau: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=215,y=45)

        label = tk.Label(self.sett_reg, text="acc",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=380,y=45)

        # chk_btn = tk.Checkbutton(self.sett_reg, text="Check IP",bg='white', variable=self.check_ip, font=("Times New Roman", 12, "bold"))
        # chk_btn.place(x=215,y=45)


        solanreg = tk.Spinbox(self.sett_reg, from_=0, to=10000000000000,width=10,
                                textvariable = self.solanreg, font=("Arial", 10, "bold")).place(x=85,y=18)

        tab_ldplayer = tk.Spinbox(self.sett_reg, from_=0, to=10000000000000,width=10,
                                textvariable = self.tab_ldplayer, font=("Arial", 10, "bold")).place(x=300,y=18)
        
        timechootp = tk.Spinbox(self.sett_reg, from_=0, to=10000000000000,width=10,
                                textvariable = self.timechootp, font=("Arial", 10, "bold")).place(x=115,y=48)
        
        timechootp = tk.Spinbox(self.sett_reg, from_=0, to=10000000000000,width=10,
                                textvariable = self.doiipsau, font=("Arial", 10, "bold")).place(x=290,y=48)
        
    def setting_LDPlayer(self):
        self.sett_ld = tk.Frame(self.Setting,background='white',highlightbackground='black',
                    highlightthickness=2)
        self.sett_ld.pack(side=tk.LEFT,fill="both", expand=True)
        self.sett_ld.pack_propagate(False)
        self.sett_ld.configure(width = 450, height = 180  )
        self.sett_ld.place(x=410,y=150)

        #--------------------------------------------------Cấu Hình LDPlayer-----------------------------------------------

        self.chedold = tk.IntVar()
        self.delayopenLD = tk.IntVar()
        self.openmin = tk.StringVar()
        self.openmax = tk.StringVar()
        self.closemin = tk.StringVar()
        self.closemax = tk.StringVar()
        self.pathldplayer = tk.StringVar()

        label = tk.Label(self.Setting, text="Cấu Hình LDPlayer",fg='black',bg='white', font=("Arial", 15, "bold"))
        label.place(x=410,y=130)

        label = tk.Label(self.sett_ld, text="Chế độ chạy LDPlayer: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=15)

        label = tk.Label(self.sett_ld, text="Mở LDPlayer: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=75)

        label = tk.Label(self.sett_ld, text="Đến ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=340,y=75)

        label = tk.Label(self.sett_ld, text="Đến ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=225,y=110)

        label = tk.Label(self.sett_ld, text="Delay đóng LDPlayer: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=110)

        label = tk.Label(self.sett_ld, text="Đường dẫn LDPlayer: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=145)

        chk_btn = tk.Radiobutton(self.sett_ld, text="Thường(1 tài khoản/1 LDPLayer)",bg='white', variable=self.chedold,value=1, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=160,y=15)

        chk_btn = tk.Radiobutton(self.sett_ld, text="Swap(Nhiều tài khoản/1 LDPLayer)",bg='white', variable=self.chedold,value=2, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=160,y=45)

        chk_btn = tk.Checkbutton(self.sett_ld, text="Delay Mở: ",bg='white', variable=self.delayopenLD, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=160,y=75)

        spinbox = tk.Spinbox(self.sett_ld, from_=0, to=10000000000000,width=5,
                                textvariable = self.openmin, font=("Arial", 10, "bold")).place(x=280,y=77)
        
        spinbox = tk.Spinbox(self.sett_ld, from_=0, to=10000000000000,width=5,
                                textvariable = self.openmax, font=("Arial", 10, "bold")).place(x=390,y=77)
        
        spinbox = tk.Spinbox(self.sett_ld, from_=0, to=10000000000000,width=5,
                                textvariable = self.closemin, font=("Arial", 10, "bold")).place(x=160,y=112)
        
        spinbox = tk.Spinbox(self.sett_ld, from_=0, to=10000000000000,width=5,
                                textvariable = self.closemax, font=("Arial", 10, "bold")).place(x=280,y=112)
        
        entry = tk.Entry(self.sett_ld, width=35, bd =0,textvariable=self.pathldplayer, font=('Arial 10'), borderwidth=2, relief="solid")
        entry.pack(padx=5, pady=5)
        entry.place(x=160,y=145, height=20)
    
    def setting_ip(self):
        self.sett_ip = tk.Frame(self.Setting,background='white',highlightbackground='black',
                    highlightthickness=2)
        self.sett_ip.pack(side=tk.LEFT,fill="both", expand=True)
        self.sett_ip.pack_propagate(False)
        self.sett_ip.configure(width = 450, height = 350  )
        self.sett_ip.place(x=410,y=360)

        self.proxy = tk.Frame(self.sett_ip,background='white',highlightbackground='black',
                    highlightthickness=2)
        self.proxy.pack(side=tk.LEFT,fill="both", expand=True)
        self.proxy.pack_propagate(False)
        self.proxy.configure(width = 420, height = 250  )
        self.proxy.place(x=10,y=80)

        self.notebook = ttk.Notebook(self.proxy)
        self.notebook.pack(fill="both", expand=True)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text='Proxy có sẵn')
        self.notebook.add(self.tab2, text='Tmproxy')
        self.notebook.add(self.tab3, text='proxymxh')

        self.proxy_co_san = tk.Frame(self.tab1,bg='white',highlightbackground='black',
                highlightthickness=2)
        self.proxy_co_san.pack(side=tk.LEFT,fill="both", expand=True)
        self.proxy_co_san.pack_propagate(False)
        self.proxy_co_san.configure(width = 1100, height = 850  )
        self.proxy_co_san.place(x=0,y=0)

        self.tm_proxy = tk.Frame(self.tab2,bg='white',highlightbackground='black',
                highlightthickness=2)
        self.tm_proxy.pack(side=tk.LEFT,fill="both", expand=True)
        self.tm_proxy.pack_propagate(False)
        self.tm_proxy.configure(width = 1100, height = 850  )
        self.tm_proxy.place(x=0,y=0)

        self.proxymxh = tk.Frame(self.tab3,bg='white',highlightbackground='black',
                highlightthickness=2)
        self.proxymxh.pack(side=tk.LEFT,fill="both", expand=True)
        self.proxymxh.pack_propagate(False)
        self.proxymxh.configure(width = 1100, height = 850  )
        self.proxymxh.place(x=0,y=0)


        #--------------------------------------------------Cấu Hình IP-----------------------------------------------

        self.doiip = tk.IntVar()
        self.typeproxy = tk.IntVar()
        self.webproxy = tk.IntVar()

        label = tk.Label(self.Setting, text="Cấu Hình Đổi IP",fg='black',bg='white', font=("Arial", 15, "bold"))
        label.place(x=410,y=340)

        label = tk.Label(self.proxy_co_san, text="IP:Port hoặc IP:Port:User:Password",fg='black',bg='white', font=("Arial", 10, "bold"))
        label.place(x=10,y=10)

        label = tk.Label(self.proxymxh, text="IP:Port hoặc IP:Port:User:Password",fg='black',bg='white', font=("Arial", 10, "bold"))
        label.place(x=10,y=45)

        label = tk.Label(self.proxy_co_san, text="Loại Proxy: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=40)

        label = tk.Label(self.proxy_co_san, text="Danh sách Proxy(_): ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=70)

        label = tk.Label(self.proxy_co_san, text="(Mỗi proxy 1 dòng)",fg='red',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=280,y=70)

        label = tk.Label(self.proxymxh, text="(https://proxymxh.com/)",fg='blue', bg='white',font=("Times New Roman", 12, "normal"))
        label.place(x=250,y=11)

        label = tk.Label(self.proxymxh, text="Điền KEY proxy web",fg='black', bg='white',font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=75)

        chk_btn = tk.Radiobutton(self.sett_ip, text="Không đổi IP",bg='white', variable=self.doiip,value=1, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=15)

        chk_btn = tk.Radiobutton(self.sett_ip, text="Không đổi IP",bg='white', variable=self.doiip,value=1, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=15)

        chk_btn = tk.Radiobutton(self.sett_ip, text="Đổi IP HMA",bg='white', variable=self.doiip,value=2, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=250,y=15)

        chk_btn = tk.Radiobutton(self.sett_ip, text="Đổi IP Hotspot Shield",bg='white', variable=self.doiip,value=4, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=250,y=45)

        chk_btn = tk.Radiobutton(self.sett_ip, text="PROXY",bg='white', variable=self.doiip,value=3, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=45)

        chk_btn = tk.Radiobutton(self.proxy_co_san, text="HTTP và HTTPS",bg='white', variable=self.typeproxy,value=1, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=100,y=40)

        chk_btn = tk.Radiobutton(self.proxy_co_san, text="SOCKS5",bg='white', variable=self.typeproxy,value=2, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=280,y=40)

        chk_btn = tk.Radiobutton(self.proxymxh, text="Đổi Proxy qua proxymxh",fg='red',bg='white', variable=self.webproxy,value=1, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=10)

        chk_btn = tk.Radiobutton(self.proxy_co_san, text="Đổi Proxy có sẳn",fg='red',bg='white', variable=self.webproxy,value=2, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=250,y=10)

        self.keyproxy = tk.Text(self.proxymxh, height=35, width=48,)
        self.keyproxy.place(x=10, y=100)

        self.proxy_available = tk.Text(self.proxy_co_san, height=35, width=48)
        self.proxy_available.place(x=10, y=100)

        # Tạo scrollbar cho widget Text
        scrollbar = tk.Scrollbar(self.proxy_co_san, command=self.proxy_available.yview)
        scrollbar.place(x=390, y=100, height=150)

        # Liên kết scrollbar với widget Text
        self.proxy_available.config(yscrollcommand=scrollbar.set)

    def setting_account(self):

        self.sett_ac = tk.Frame(self.Setting,background='white',highlightbackground='black',
                    highlightthickness=2)
        self.sett_ac.pack(side=tk.LEFT,fill="both", expand=True)
        self.sett_ac.pack_propagate(False)
        self.sett_ac.configure(width = 450, height = 240  )
        self.sett_ac.place(x=880,y=30)

        #--------------------------------------------------Cấu Hình Account-----------------------------------------------

        self.nameaccount = tk.IntVar()
        self.password = tk.IntVar()
        self.random_password = tk.IntVar()
        self.oldmin = tk.StringVar()
        self.oldmax = tk.StringVar()
        self.sex = tk.IntVar()
        self.bm2fa = tk.IntVar()
        self.avata = tk.IntVar()
        self.bia = tk.IntVar()
        self.pathanhavt = tk.IntVar()

        label = tk.Label(self.Setting, text="Cấu Hình Tài Khoản",fg='black',bg='white', font=("Arial", 15, "bold"))
        label.place(x=880,y=15)

        label = tk.Label(self.sett_ac, text="Tên đăng ký: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=15)

        label = tk.Label(self.sett_ac, text="Mật khẩu facebook: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=45)

        label = tk.Label(self.sett_ac, text="Độ tuổi: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=75)

        label = tk.Label(self.sett_ac, text="Giới tính: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=105)

        label = tk.Label(self.sett_ac, text="đền",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=150,y=75)
        

        chk_btn = tk.Radiobutton(self.sett_ac, text="Tên Việt",bg='white', variable=self.nameaccount,value=1, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=90,y=15)

        chk_btn = tk.Radiobutton(self.sett_ac, text="Tên ngoại",bg='white', variable=self.nameaccount,value=2, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=180,y=15)

        chk_btn = tk.Radiobutton(self.sett_ac, text="Nam",bg='white', variable=self.sex,value=1, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=80,y=105)

        chk_btn = tk.Radiobutton(self.sett_ac, text="Nữ",bg='white', variable=self.sex,value=2, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=140,y=105)

        chk_btn = tk.Radiobutton(self.sett_ac, text="Ngẫu Nhiên",bg='white', variable=self.sex,value=3, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=200,y=105)

        chk_btn = tk.Checkbutton(self.sett_ac, text="Ngẫu Nhiên",bg='white', variable=self.random_password, font=("Times New Roman", 12, "bold"))
        chk_btn.place(x=300,y=44)

        chk_btn = tk.Checkbutton(self.sett_ac, text="Đặt bảo mật 2 lớp (2FA)",bg='white', variable=self.bm2fa, font=("Times New Roman", 12, "bold"))
        chk_btn.place(x=10,y=135)
        
        chk_btn = tk.Checkbutton(self.sett_ac, text="Thay avata",bg='white', variable=self.avata, font=("Times New Roman", 12, "bold"))
        chk_btn.place(x=10,y=165)

        chk_btn = tk.Checkbutton(self.sett_ac, text="Thay ảnh bìa",bg='white', variable=self.bia, font=("Times New Roman", 12, "bold"))
        chk_btn.place(x=10,y=195)

        entry = tk.Entry(self.sett_ac, width=20, bd =0,textvariable=self.password, font=('Arial 10'), borderwidth=2, relief="solid")
        entry.pack(padx=5, pady=5)
        entry.place(x=140,y=46, height=20)

        entry = tk.Entry(self.sett_ac, width=30, bd =0,textvariable=self.pathanhavt, font=('Aria', 10, 'bold'), borderwidth=2, relief="solid")
        entry.pack(padx=5, pady=5)
        entry.place(x=120,y=169, height=25)

        solanreg = tk.Spinbox(self.sett_ac, from_=0, to=10000000000000,width=5,
                                textvariable = self.oldmin, font=("Arial", 10, "bold")).place(x=85,y=75)

        solanreg = tk.Spinbox(self.sett_ac, from_=0, to=10000000000000,width=5,
                                textvariable = self.oldmax, font=("Arial", 10, "bold")).place(x=200,y=75)
        
    def setting_active(self):

        self.sett_at = tk.Frame(self.Setting,background='white',highlightbackground='black',
                    highlightthickness=2)
        self.sett_at.pack(side=tk.LEFT,fill="both", expand=True)
        self.sett_at.pack_propagate(False)
        self.sett_at.configure(width = 450, height = 350  )
        self.sett_at.place(x=880,y=300)

        #--------------------------------------------------Cấu Hình Active-----------------------------------------------


        self.active = tk.IntVar()
        self.api = tk.StringVar()
        self.maill = tk.IntVar()
        self.mkmail = tk.IntVar()
        self.randommail = tk.IntVar()
        self.tempmail = tk.IntVar()
        
        self.thuesdt = tk.Frame(self.sett_at,background='white',highlightbackground='black',
                    highlightthickness=2)
        self.thuesdt.pack(side=tk.LEFT,fill="both", expand=True)
        self.thuesdt.pack_propagate(False)
        self.thuesdt.configure(width = 420, height = 70  )
        self.thuesdt.place(x=10,y=45)

        self.mail = tk.Frame(self.sett_at,background='white',highlightbackground='black',
                    highlightthickness=2)
        self.mail.pack(side=tk.LEFT,fill="both", expand=True)
        self.mail.pack_propagate(False)
        self.mail.configure(width = 420, height = 180  )
        self.mail.place(x=10,y=150)

        self.notebook = ttk.Notebook(self.mail)
        self.notebook.pack(fill="both", expand=True)

        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab3, text='Temp Mail')
        self.notebook.add(self.tab1, text='Mail TM')
        self.notebook.add(self.tab2, text='Hotmail')
        
        label = tk.Label(self.Setting, text="Cấu Hình Xác minh",fg='black',bg='white', font=("Arial", 15, "bold"))
        label.place(x=880,y=285)

        label = tk.Label(self.thuesdt, text="Chọn dịch vụ sms: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=0)

        label = tk.Label(self.thuesdt, text="API:",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=30)

        label = tk.Label(self.tab1, text="Mật khẩu mail:",fg='black', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=30)

        label = tk.Label(self.tab1, text="(Mỗi dòng 1 mail)",fg='red', font=("Times New Roman", 12, "normal"))
        label.place(x=300,y=60)
        
        label = tk.Label(self.tab3, text="(https://temp-mail.io/)",fg='blue', font=("Times New Roman", 12, "normal"))
        label.place(x=280,y=11)


        chk_btn = tk.Radiobutton(self.sett_at, text="Thuê số điện thoại",bg='white', variable=self.active, value=1 ,font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=15)

        chk_btn = tk.Radiobutton(self.sett_at, text="Xác nhận qua mail",bg='white', variable=self.active, value=2 ,font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=120)

        chk_btn = tk.Radiobutton(self.tab1, text="Tự động đăng ký", variable=self.mail, value=1 ,font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=0)

        chk_btn = tk.Radiobutton(self.tab1, text="Mail Tm có sẵn", variable=self.mail, value=2 ,font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=60)

        chk_btn = tk.Checkbutton(self.tab1, text="Ngẫu nhiên", variable=self.randommail ,font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=300,y=30)

        chk_btn = tk.Checkbutton(self.tab3, text="Xác minh qua temp mail",fg='red', variable=self.tempmail ,font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=10)

        entry = tk.Entry(self.thuesdt, width=25, bd =0,textvariable=self.api, font=("Times New Roman", 12, "bold"), borderwidth=2, relief="solid")
        entry.pack(padx=5, pady=5)
        entry.place(x=50,y=30, height=25)

        entry = tk.Entry(self.tab1, width=23, bd =0,textvariable=self.mkmail, font=("Times New Roman", 12, "bold"), borderwidth=2, relief="solid")
        entry.pack(padx=5, pady=5)
        entry.place(x=110,y=30, height=25)

        self.text_area = tk.Text(self.tab1, height=35, width=48)
        self.text_area.place(x=10, y=100)


    def interaction(self):

        self.tuongtac = tk.Frame(self.Setting,background='white',highlightbackground='black',
                    highlightthickness=2)
        self.tuongtac.pack(side=tk.LEFT,fill="both", expand=True)
        self.tuongtac.pack_propagate(False)
        self.tuongtac.configure(width = 450, height = 350  )
        self.tuongtac.place(x=880,y=680)

        #--------------------------------------------------Tương tác sau khi reg thành công-----------------------------------------------

        self.seen_Notification = tk.IntVar()

        label = tk.Label(self.Setting, text="Tương tác sau khi reg thành công",fg='black',bg='white', font=("Arial", 15, "bold"))
        label.place(x=880,y=665)

        chk_btn = tk.Checkbutton(self.tuongtac, text="Đọc thông công",bg='white', variable=self.seen_Notification ,font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=0,y=10)
    def button(self):

        frame = tk.Frame(self.Setting, highlightbackground="green", highlightcolor="green", highlightthickness=2, bd=0)
        frame.configure(width = 100, height = 50  )
        frame.place(x=10,y=10)

        frame1 = tk.Frame(self.Setting, highlightbackground="red", highlightcolor="red", highlightthickness=2, bd=0)
        frame1.configure(width = 100, height = 50  )
        frame1.place(x=120,y=10)

        frame2 = tk.Frame(self.Setting, highlightbackground="orange", highlightcolor="orange", highlightthickness=2, bd=0)
        frame2.configure(width = 100, height = 50  )
        frame2.place(x=230,y=10)

        frame3 = tk.Frame(self.Setting, highlightbackground="blue", highlightcolor="blue", highlightthickness=2, bd=0)
        frame3.configure(width = 130, height = 50  )
        frame3.place(x=340,y=10)

        frame4 = tk.Frame(self.Setting, highlightbackground="purple", highlightcolor="purple", highlightthickness=2, bd=0)
        frame4.configure(width = 130, height = 50  )
        frame4.place(x=10,y=60)

        frame5 = tk.Frame(self.Setting, highlightbackground="brown", highlightcolor="brown", highlightthickness=2, bd=0)
        frame5.configure(width = 100, height = 50  )
        frame5.place(x=121,y=60)

        frame6 = tk.Frame(self.Setting, highlightbackground="purple", highlightcolor="purple", highlightthickness=2, bd=0)
        frame6.configure(width = 130, height = 50  )
        frame6.place(x=250,y=60)

  
        
        custom_font = tkfont.Font(family="Helvetica", size=10, weight="bold")

        button = tk.Button(frame, text="Bắt Đầu",command=self.run, bg="white", fg="green", width=12, height=2,bd=0, font=custom_font,relief="solid",)
        button.pack()

        button = tk.Button(frame1, text="Dừng lại", bg="white", fg="red", width=12, height=2,bd=0, font=custom_font,relief="solid",)
        button.pack()

        button = tk.Button(frame2, text="Lưu cấu hình", bg="white", fg="orange", width=12, height=2,bd=0, font=custom_font,relief="solid",
                           command=self.save_setting)
        button.pack()

        button = tk.Button(frame3, text="Cài đặt nâng cao", bg="white", fg="blue", width=14, height=2,bd=0, font=custom_font,relief="solid",
                           command=self.button_setting_Advanced)
        button.pack()

        button = tk.Button(frame4, text="Output Data", bg="white", fg="purple", width=12, height=2,bd=0, font=custom_font,relief="solid")
        button.pack()

        button = tk.Button(frame5, text="Quản lí LDPlayer", bg="white", fg="brown", width=14, height=2,bd=0, font=custom_font,relief="solid")
        button.pack()

        button = tk.Button(frame6, text="Tạo mới LDPlayer", bg="white", fg="purple", width=14, height=2,bd=0, font=custom_font,relief="solid"
                           ,command=self.button_createldplayer)
        button.pack()
    def account(self):

        self.act_list = tk.Frame(self.accountt,highlightbackground='black',
                    highlightthickness=2)
        self.act_list.pack(side=tk.LEFT,fill="both", expand=True)
        self.act_list.pack_propagate(False)
        self.act_list.configure(width = 1320, height = 850  )
        self.act_list.place(x=10,y=10)
        
        scrollbar = tk.Scrollbar(self.act_list, orient="vertical")
        scrollbar.pack(side="right", fill="y")


        style = ttk.Style(self.root)
        style.configure(style="Treeview", height=10)
        self.thanhchinh = ttk.Treeview(self.act_list, yscrollcommand=scrollbar.set) 
        self.thanhchinh.configure(style="Treeview", height=50)
        self.thanhchinh.pack(expand=True, fill="both")
        self.thanhchinh["columns"] = ("one", "two", "three")
        self.thanhchinh["columns"] = ("one", "two", "three", "four", "five", 'six','seven','eight','nine','ten','eleven','twelve')
        self.thanhchinh.column("one", width=50)
        self.thanhchinh.column("two", width=100)
        self.thanhchinh.column("three", width=100)
        self.thanhchinh.column("four", width=100)
        self.thanhchinh.column("five", width=100)
        self.thanhchinh.column("six", width=100 )
        self.thanhchinh.column("seven", width=100)
        self.thanhchinh.column("eight", width=100)
        self.thanhchinh.column("nine", width=150)
        self.thanhchinh.column("ten", width=100)
        self.thanhchinh.column("eleven", width=200)
        self.thanhchinh.column("twelve", width=50)
        self.thanhchinh.heading("one", text="Index")
        self.thanhchinh.heading("two", text="Device ID")
        self.thanhchinh.heading("three", text="Device Name")
        self.thanhchinh.heading("four", text="Proxy")
        self.thanhchinh.heading("five", text="Name")
        self.thanhchinh.heading("six", text="Birthday")
        self.thanhchinh.heading("seven", text="Gender")
        self.thanhchinh.heading("eight", text="Password")
        self.thanhchinh.heading("nine", text="Email")
        self.thanhchinh.heading("ten", text="Otp")
        self.thanhchinh.heading("eleven", text="Status")
        self.thanhchinh.heading("twelve", text="Time")
        self.thanhchinh['show'] = 'headings'
    def button_setting_Advanced(self):
        toplevel = tk.Toplevel(self.root)
        toplevel.title("Cài đặt nâng cao")
        toplevel.geometry('350x400')

        self.toplevel = tk.Frame(toplevel,background='white')
        self.toplevel.pack(side=tk.LEFT,fill="both", expand=True)
        self.toplevel.pack_propagate(False)
        self.toplevel.configure(width = 350, height = 400  )
        self.toplevel.place(x=0,y=0)

        #-------------------------------------------------Cài đặt nâng cao-----------------------------------------------

        self.CPU = tk.StringVar()
        self.RAM = tk.StringVar()
        self.WIDTH = tk.StringVar()
        self.HEIGHT = tk.StringVar()
        self.GPS = tk.IntVar()
        self.CACHE = tk.IntVar()
        self.ADB = tk.IntVar()
        self.OTHER = tk.IntVar()
        self.DPI = tk.IntVar()
        self.pathTesseractOCR = tk.StringVar()
        

        self.setting_ld = tk.Frame(self.toplevel,background='white',highlightbackground='black',
                    highlightthickness=1)
        self.setting_ld.pack(side=tk.LEFT,fill="both", expand=True)
        self.setting_ld.pack_propagate(False)
        self.setting_ld.configure(width = 350, height = 200  )
        self.setting_ld.place(x=0,y=15)

        self.Other_functions = tk.Frame(self.toplevel,background='white',highlightbackground='black',
                    highlightthickness=1)
        self.Other_functions.pack(side=tk.LEFT,fill="both", expand=True)
        self.Other_functions.pack_propagate(False)
        self.Other_functions.configure(width = 350, height = 200  )
        self.Other_functions.place(x=0,y=230)

        frame = tk.Frame(self.toplevel, highlightbackground="green", highlightcolor="green", highlightthickness=2, bd=0)
        frame.configure(width = 300, height = 50  )
        frame.place(x=0,y=356)

        label = tk.Label(self.toplevel, text="Cấu hình LDPlayer",fg='black',bg='white', font=("Arial", 15, "bold"))
        label.place(x=0,y=0)

        label = tk.Label(self.toplevel, text="Chức năng khác",fg='black',bg='white', font=("Arial", 15, "bold"))
        label.place(x=0,y=215)

        label = tk.Label(self.setting_ld, text="CPU: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=16)

        label = tk.Label(self.setting_ld, text="RAM: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=46)

        label = tk.Label(self.setting_ld, text="SIZE: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=76)

        label = tk.Label(self.setting_ld, text="X ",fg='black',bg='white', font=("Airbnb Cereal", 15, "bold"))
        label.place(x=110,y=76)

        label = tk.Label(self.setting_ld, text="DPI: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=106)

        label = tk.Label(self.Other_functions, text="Loại App: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=16)

        label = tk.Label(self.Other_functions, text="Đường dẫn tới Tesseract-OCR: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=46)

        list_cpu = ["1 Core (Đề xuất)", "2 Core", "3 Core", "4 Core"]
        list_ram = ["512 M","768 M","1024 M (Đề xuất)", "1536 M", "2048 M", "3072 M"]


        combobox = ttk.Combobox(self.toplevel, textvariable=self.CPU, values=list_cpu, font=("Times New Roman", 12, "normal"))
        combobox.place(x=60,y=33)
        combobox.set("1 Core (Đề xuất)")

        combobox = ttk.Combobox(self.toplevel, textvariable=self.RAM, values=list_ram, font=("Times New Roman", 12, "normal"))
        combobox.place(x=60,y=63)
        combobox.set("1024 M (Đề xuất)")

        spinbox = tk.Spinbox(self.toplevel, from_=0, to=10000000000000,width=5,
                                textvariable = self.WIDTH, font=("Arial", 10, "bold")).place(x=60,y=96)
        
        spinbox = tk.Spinbox(self.toplevel, from_=0, to=10000000000000,width=5,
                                textvariable = self.HEIGHT, font=("Arial", 10, "bold")).place(x=135,y=96)
        
        spinbox = tk.Spinbox(self.toplevel, from_=0, to=10000000000000,width=5,
                                textvariable = self.DPI, font=("Arial", 10, "bold")).place(x=60,y=126)
        
        chk_btn = tk.Checkbutton(self.toplevel, text="Bật GPS LDPlayer",bg='white', variable=self.GPS, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=150)

        chk_btn = tk.Checkbutton(self.toplevel, text="Tự động clear cache LDPlayer",bg='white', variable=self.CACHE, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=170)

        chk_btn = tk.Checkbutton(self.toplevel, text="ADB Debug (Dành cho các phiên bản LDPlayer cao hơn)",bg='white', variable=self.ADB, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=190)

        chk_btn = tk.Radiobutton(self.Other_functions, text="Facebook katana",bg='white', variable=self.OTHER,value=1, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=75,y=15)

        chk_btn = tk.Radiobutton(self.Other_functions, text="Facebook Lite",bg='white', variable=self.OTHER,value=2, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=215,y=15)

        custom_font = tkfont.Font(family="Helvetica", size=10, weight="bold")

        button = tk.Button(frame, text="Lưu cấu hình", bg="green", fg="black", width=43, height=2,bd=0, font=custom_font,relief="solid",
                           command=self.save_Advanced_settings)
        button.pack()

        entry = tk.Entry(self.Other_functions, width=35, bd =0,textvariable=self.pathTesseractOCR, font=('Arial 10'), borderwidth=2, relief="solid")
        entry.pack(padx=5, pady=5)
        entry.place(x=10,y=76, height=20)

       

    def button_createldplayer(self):
        toplevel = tk.Toplevel(self.root)
        toplevel.title("Cài đặt nâng cao")
        toplevel.geometry('450x250')

        self.toplevel = tk.Frame(toplevel,background='white')
        self.toplevel.pack(side=tk.LEFT,fill="both", expand=True)
        self.toplevel.pack_propagate(False)
        self.toplevel.configure(width = 450, height = 250  )
        self.toplevel.place(x=0,y=0)

        #-------------------------------------------------Cài đặt nâng cao-----------------------------------------------
        
        self.VERSION = tk.StringVar()
        self.CREATE = tk.StringVar()
        self.MANAGER = tk.IntVar()
        
        self.create_ld = tk.Frame(self.toplevel,background='white',highlightbackground='black',
                    highlightthickness=1)
        self.create_ld.pack(side=tk.LEFT,fill="both", expand=True)
        self.create_ld.pack_propagate(False)
        self.create_ld.configure(width = 450, height = 250  )
        self.create_ld.place(x=0,y=17)

        frame = tk.Frame(self.toplevel, highlightbackground="green", highlightcolor="green", highlightthickness=2, bd=0)
        frame.configure(width = 300, height = 50  )
        frame.place(x=0,y=207)

        label = tk.Label(self.toplevel, text="Tạo mới LDPlayer",fg='black',bg='white', font=("Arial", 15, "bold"))
        label.place(x=0,y=0)

        label = tk.Label(self.create_ld, text="Phiên bản LDPlayer: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=16)

        label = tk.Label(self.create_ld, text="Số tạo mới: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=56)

        label = tk.Label(self.create_ld, text="Quản lí ổ cứng: ",fg='black',bg='white', font=("Times New Roman", 12, "normal"))
        label.place(x=10,y=96)

        list_version = ["Android 9.0 (64-bit) (Đề xuất)","Android 7.1 (32-bit)","Android 7.1 (64-bit)", "Android 5.1 (32-bit)"]

        combobox = ttk.Combobox(self.toplevel, textvariable=self.VERSION, values=list_version, font=("Times New Roman", 12, "normal"))
        combobox.place(x=150,y=33)
        combobox.set("Android 9.0 (64-bit) (Đề xuất)")

        spinbox = tk.Spinbox(self.toplevel, from_=0, to=10000000000000,width=5,
                                textvariable = self.CREATE, font=("Arial", 10, "bold")).place(x=150,y=76)
        
        chk_btn = tk.Radiobutton(self.toplevel, text="Tự động mở rộng (Đề xuất)",bg='white', variable=self.MANAGER,value=1, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=136)

        chk_btn = tk.Radiobutton(self.toplevel, text="Quản lí thủ công",bg='white', variable=self.MANAGER,value=2, font=("Times New Roman", 12, "normal"))
        chk_btn.place(x=10,y=156)

        custom_font = tkfont.Font(family="Helvetica", size=10, weight="bold")

        button = tk.Button(frame, text="Lưu cấu hình", bg="green", fg="black", width=55, height=2,bd=0, font=custom_font,relief="solid",)
        button.pack()

    def save_Advanced_settings(self):
        CPU = self.CPU.get()
        RAM = self.RAM.get()
        WIDTH = self.WIDTH.get()
        HEIGHT = self.HEIGHT.get()
        CACHE = self.CACHE.get()
        OTHER = self.OTHER.get()
        ADB = self.ADB.get()
        DPI = self.DPI.get()
        pathTesseractOCR = self.pathTesseractOCR.get()
        manager().Advanced_settings(CPU,RAM,WIDTH,HEIGHT,DPI,CACHE,OTHER,ADB,pathTesseractOCR)

    def save_setting_reg(self):
        solanreg = self.solanreg.get()
        tab_ldplayer = self.tab_ldplayer.get()
        timechootp = self.timechootp.get()
        doiipsau = self.doiipsau.get()
        manager().setting_reg(solanreg,tab_ldplayer,timechootp,doiipsau)

    def save_setting_ld(self):
        chedold = self.chedold.get()
        delayopenLD = self.delayopenLD.get()
        openmin = self.openmin.get()
        openmax = self.openmax.get()
        closemin = self.closemin.get()
        closemax = self.closemax.get()
        pathldplayer = self.pathldplayer.get()
        manager().setting_ld(chedold,delayopenLD,openmin,openmax,closemin,closemax,pathldplayer)

    def save_setting_ip(self):
        doiip = self.doiip.get()
        webproxy = self.webproxy.get()
        if webproxy == 1:
            text_content = self.keyproxy.get("1.0", tk.END)
        else:
            text_content = self.proxy_available.get("1.0", tk.END)
        manager().setting_ip(doiip,webproxy,text_content)

    def save_setting_account(self):
        nameaccount = self.nameaccount.get()
        password = self.password.get()
        random_password = self.random_password.get()
        oldmin = self.oldmin.get()
        oldmax = self.oldmax.get()
        sex = self.sex.get()
        bm2fa = self.bm2fa.get()
        avata = self.avata.get()
        bia = self.bia.get()
        pathanhavt = self.pathanhavt.get()
        manager().setting_account(nameaccount,password,random_password,oldmin,oldmax,sex,bm2fa,avata,bia,pathanhavt)
    def save_setting_active(self):
        active = self.active.get()
        api = self.api.get()
        maill = self.maill.get()
        mkmail = self.mkmail.get()
        randommail = self.randommail.get()
        tempmail = self.tempmail.get()
        manager().setting_active(active,api,maill,mkmail,randommail,tempmail)
    def save_setting(self):
        self.save_setting_active()
        self.save_setting_account()
        self.save_setting_ip()
        self.save_setting_ld()
        self.save_setting_reg()
    
        
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
#             giaodien().tab()
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


giaodien().tab()