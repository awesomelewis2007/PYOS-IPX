#ipx a mod for PYOS

import colour
from colr import color
adderss =None
import socket
import os
import time
os.system("cls")
import socket 


#==============================logos==============================
def no_glitch():
    print("""
                                     ___  ________  ___    ___ 
                                    |\  \|\   __  \|\  \  /  /|
                                    \ \  \ \  \|\  \ \  \/  / /
                                     \ \  \ \   ____\ \    / / 
                                      \ \  \ \  \___|/     \/  
                                       \ \__\ \__\  /  /\   \  
                                        \|__|\|__| /__/ /\ __\ 
                                                   |__|/ \|__| 

















VER 4.5
    """)
#======================================================

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 

#===================================================
os.system("color 08")   
no_glitch()
os.system("color 08")
time.sleep(0.4)
os.system("color 07")
time.sleep(0.4)
os.system("color 0f")
time.sleep(1)

os.system("color 0f")
time.sleep(0.4)
os.system("color 07")
time.sleep(0.4)
os.system("color 08")
os.system("cls")
os.system("cls")
os.system("color 07")
#======================MAIN SCRIPT===============================








print(color('                                                        IPX.[SERVERSIDE]                                               ', fore='blue', style='h',back="white"))
print(color('                                                  (C)PYOS-SYSTEMS 2020 [beata]                                         ', fore='blue', style='h',back="white"))
print("=============================================")
print("Local ip address:",IPAddr)
print("Computer name   :",hostname)
while True:
    import os
    print("=============================================")
    ipxcommand = input("[IN] Server>")
    print("=============================================")
    if ipxcommand == "exit":
        exit()



    if ipxcommand == "ip":
        print("[OUT]")
        os.system("ipconfig")



    if ipxcommand == "ip all":
        print("[OUT]")
        os.system(r"ipconfig /all")



    if ipxcommand == "ip renew":
        print("[OUT]")
        try:
            os.system("ipconfig /renew")
        except:
            print("[X] ERROR CANT RENEW IP")



    if ipxcommand == "gdi": 
        import socket
        address = input("[IN] GDI>")
        print("[OUT]")
        print(socket.getaddrinfo(address, 80, proto=socket.IPPROTO_TCP))


    if ipxcommand == "macinfo":
        print("[OUT]")
        os.system("getmac")



    if ipxcommand == "fullmac":
        print("[OUT]")
        os.system("getmac /v /fo list")



    if ipxcommand == "network":
        print("[OUT]")
        print("===================ipx list=============================")
        os.system("NET VIEW")



    if ipxcommand == "iplook":
        hostinputdir = "null"
        hostinputdir = input("[IN]hostdir>")
        print("[OUT]")
        try:
            print(socket.gethostbyname(hostinputdir)) # your os sends out a dns query
        except:
            print("[X] ERROR CANT SEND DNS")

    
    if ipxcommand == "urllook":
        from urllib.request import Request, urlopen, urlretrieve
        from bs4 import BeautifulSoup
        import time
        def read_url(url):
            try:
                url = url.replace(" ","%20")
                req = Request(url)
                a = urlopen(req).read()
                soup = BeautifulSoup(a, 'html.parser')
                x = (soup.find_all('a'))
                print("=============================================")
                time.sleep(0.3)
                print("[OUT]")
                for i in x:
                    try:
                        file_name = i.extract().get_text()
                        url_new = url +"/"+ file_name
                        url_new = url_new.replace(" ","%20")
                        if(file_name[-1]=='/' and file_name[0]!='.'):
                            read_url(url_new)
                        print(url_new)
                    except:
                        print("[X] ERROR cant show URL!")
            except:
                print("[X] ERROR forbidden or not a URL")
        urlinput = input("http url>")
        read_url(urlinput)
    if ipxcommand == "htmlrip":
        import requests
        urlxxxx = input("URL>")
        page = requests.get(urlxxxx)
        contents = page.content
        print(contents)
        








    if ipxcommand == "help":
        print("""
=======================ipx help========================
no|command    |description
=======================================================
1 |exit       |exits the mod
2 |ip         |displays ip infomation
3 |ip all     |displays all of the ip infomation
4 |ip renew   |renews the ip using windosw ip renew
5 |gdi        |gets address info on a ip or hoast name
6 |help       |this help msg
7 |macinfo    |displays the mac info
8 |fullmac    |displays the fullmac
9 |network    |displays all of the users on your network
10|iplook     |gets an ip from a host name
11|urllook    |looks up all the sub urls in a http       
        """)
