import json
class manager:
    def Advanced_settings(self,CPU,RAM,WIDTH,HEIGHT,DPI,CACHE,OTHER,ADB,pathTesseractOCR):

        # Tạo một đối tượng ConfigParser
        config_data = {
            'CPU': f'{CPU.split()[0]}',
            'RAM': f'{RAM.split()[0]}',
            'WIDTH': f'{WIDTH}',
            'HEIGHT': f'{HEIGHT}',
            'DPI': f'{DPI}',
            'CACHE': f'{CACHE}',
            'OTHER': f'{OTHER}',
            'ADB': f'{ADB}',
            'pathTesseractOCR': pathTesseractOCR
        }

        with open('Advanced_settings.json', 'w',encoding='utf-8') as configfile:
            json.dump(config_data, configfile, indent=4)
    def setting_reg(self,solanreg,tab_ldplayer,timechootp,doiipsau):
        config_data = {
            'solanreg': f'{solanreg}',
            'tab_ldplayer': f'{tab_ldplayer}',
            'timechootp': f'{timechootp}',
            'doiipsau': f'{doiipsau}',

        }

        with open('setting_reg.json', 'w',encoding='utf-8') as configfile:
            json.dump(config_data, configfile, indent=4)
    def setting_ld(self,chedold,delayopenLD,openmin,openmax,closemin,closemax,pathldplayer):
        config_data = {
            'chedold': f'{chedold}',
            'delayopenLD': {
                'openmin' : f'{openmin}',
                'openmax' : f'{openmax}',
            },
            'delaycloseLD': {
                'closemin' : f'{closemin}',
                'closemax' : f'{closemax}',
            },
            'pathldplayer': f'{pathldplayer}',

        }

        with open('setting_ld.json', 'w',encoding='utf-8') as configfile:
            json.dump(config_data, configfile, indent=4)
    def setting_ip(self,doiip,web,key):
        
        if web == 2:
            type_proxy = 'proxy_available'
            proxy = key
        elif web == 1:
            type_proxy = 'proxymxh'
            proxy = key
        config_data = {
            'setting_ip': f'{doiip}',
            'web_proxy' :  web,
            'key_proxy' : proxy.split('\n')[0]
        
        }
        with open('setting_ip.json', 'w',encoding='utf-8') as configfile:
            json.dump(config_data, configfile, indent=4)
    def setting_account(Self,nameaccount,password,random_password,oldmin,oldmax,sex,bm2fa,avata,bia,pathanhavt):
        config_data = {
            'nameaccount': f'{nameaccount}',
            'password': f'{password}',
            'random_password': f'{random_password}',
            'oldmin': f'{oldmin}',
            'oldmax': f'{oldmax}',
            'sex': f'{sex}',
            'bm2fa': f'{bm2fa}',
            'avata': f'{avata}',
            'bia': f'{bia}',
            'pathanhavt': f'{pathanhavt}',
        }

        with open('setting_account.json', 'w',encoding='utf-8') as configfile:
            json.dump(config_data, configfile, indent=4)
    def setting_active(self,active,api,mail,mkmail,randommail,tempmail):
        config_data = {
            'activesms': {
                'api' : f'{api}',
            },
            'activemail': {
                'tempmail' : {
                    'active' : tempmail
                },
                'hotmail' : {
                    'type_mail' : {
                        'mkmail' : mkmail,
                        'randommail':randommail
                    },
                }
            },
        }
        with open('setting_active.json', 'w',encoding='utf-8') as configfile:
            json.dump(config_data, configfile, indent=4)




