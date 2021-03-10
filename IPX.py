from types import TracebackType
import colour
from colr import color
adderss =None
import socket
import os
import time
import socket 
import platform


#        ::::::::::: :::::::::  :::    :::          ::::::::   ::::::::  :::    ::: :::::::::   ::::::::  :::::::::: 
#           :+:     :+:    :+: :+:    :+:         :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:         
#          +:+     +:+    +:+  +:+  +:+          +:+        +:+    +:+ +:+    +:+ +:+    +:+ +:+        +:+          
#         +#+     +#++:++#+    +#++:+           +#++:++#++ +#+    +:+ +#+    +:+ +#++:++#:  +#+        +#++:++#      
#        +#+     +#+         +#+  +#+                 +#+ +#+    +#+ +#+    +#+ +#+    +#+ +#+        +#+            
#       #+#     #+#        #+#    #+#         #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#             
#  ########### ###        ###    ###          ########   ########   ########  ###    ###  ########  ##########       
#                                                                                                                    
#                             source code for ipx                                                                                       
#
#
#==============================logos==============================

print("""
                                     ___  ________  ___    ___ 
                                    |\  \|\   __  \|\  \  /  /|
                                    \ \  \ \  \|\  \ \  \/  / /
                                     \ \  \ \   ____\ \    / / 
                                      \ \  \ \  \___|/     \/  
                                       \ \__\ \__\  /  /\   \  
                                        \|__|\|__| /__/ /\ __\ 
                                                   |__|/ \|__| 

















VER 5.2
    """)
#======================================================

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 

#===================================================
time.sleep(1)
if platform.system() == "Windows":
    os.system("cls")
if platform.system() == "Linux":
    os.system("clear")

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
        if platform.system() == "Windows":
            os.system("ipconfig")
        if platform.system() == "Linux":
            os.system("ifconfig")


    if ipxcommand == "ip all":
        print("[OUT]")
        if platform.system() == "Windows":
            os.system(r"ipconfig /all")
        if platform.system() == "Linux":
            os.system("ifconfig")



    if ipxcommand == "ip renew":
        print("[OUT]")
        if platform.system() == "Windows":
            try:
                os.system("ipconfig /renew")
            except:
                print("[X] ERROR CANT RENEW IP")
        if platform.system() == "Linux":
            print(":( sorry this command only works on windows im sorry.")


    if ipxcommand == "gdi": 
        import socket
        address = input("[IN] GDI>")
        print("[OUT]")
        print(socket.getaddrinfo(address, 80, proto=socket.IPPROTO_TCP))


    if ipxcommand == "macinfo":
        print("[OUT]")
        if platform.system() == "Windows":
            os.system("getmac")
        if platform.system() == "Linux":
            print(":( sorry this command only works on windows im sorry.")



    if ipxcommand == "fullmac":
        print("[OUT]")
        if platform.system() == "Windows":
            os.system("getmac /v /fo list")
        if platform.system() == "Linux":
            print(":( sorry this command only works on windows im sorry.")


    if ipxcommand == "network":
        print("[OUT]")
        print("===================ipx list=============================")
        if platform.system() == "Windows":
            os.system("netlist")
        if platform.system() == "Linux":
            print(":( sorry this command only works on windows im sorry.")



    if ipxcommand == "iplook":
        hostinputdir = "null"
        hostinputdir = input("[IN]hostdir>")
        print("[OUT]")
        try:
            print(color(socket.gethostbyname(hostinputdir),fore="green")) # your os sends out a dns query
        except:
            print(color("[X] ERROR CANT SEND DNS",fore="red"))

    
    if ipxcommand == "urllook":
        import datetime
        from urllib.request import Request, urlopen, urlretrieve
        from bs4 import BeautifulSoup
        import time
        def read_url(url):
            try:
                url = url.replace(" ","%20")
                req = Request(url)
                a = urlopen(req).read()
                soup = BeautifulSoup(a, 'html.parser')
                soup.head.append('body {background-color:#b0c4de;}')
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
                        time.sleep(0.1)
                        print(color(url_new,fore="green"))
                    except:
                        print(color("[X] ERROR cant show URL!",fore="red"))
            except:
                print(color("[X] ERROR forbidden or not a URL",fore="red"))
        urlinput = input("http url>")
        read_url(urlinput)
    if ipxcommand == "htmlrip":
        import requests
        from bs4 import BeautifulSoup

        URL = input("HTTP URL>")
        try:
            page = requests.get(URL)

            soup = BeautifulSoup(page.content, 'html.parser')
            head = soup.head
            head.append(soup.new_tag('style', type='text/css'))
            head.style.append('body {background-color:#b0c4de;}')
            print(soup)

        except ConnectionError:
            print("[X] Connection or socket.server error")

        except ConnectionAbortedError:
            print("[X] connection or syntax error")

    if ipxcommand == "filefind":    
        import requests
        from bs4 import BeautifulSoup

        def get_url_paths(url, ext='', params={}):
            try:
                response = requests.get(url, params=params)
                if response.ok:
                    response_text = response.text
                else:
                    return response.raise_for_status()
                soup = BeautifulSoup(response_text, 'html.parser')
                parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
                return parent
            except:
                print("[x] error")


        url =  input("[IN] domain:")
        ext =  input("[IN]File_ext:")
        result = get_url_paths(url, ext)
        if result != "None":
            print(result)
        if result == "None":
            pass

    if ipxcommand == "isup": 
        
        import requests
        from collections import namedtuple
        import time
        WebsiteStatus = namedtuple('WebsiteStatus', ['status_code', 'reason'])
        name = input("HTTP Domain>")
        tryn = input("ping times>")
        delay = input("ping delay>")
        attempt = 1
        try:
            tryn = int(tryn)
        except:
            print(color("[!] couldn't convert varable",fore="yellow"))
            print(color("[X] convertion error",fore="red"))
            print(color("[X] fatal please enter an intager",fore="red"))
            break
        try:
            delay = int(delay)
        except:
            print(color("[!] couldn't convert varable",fore="yellow"))
            print(color("[X] convertion error",fore="red"))
            print(color("[X] fatal please enter an intager",fore="red"))
            break

        print("==================ISUP========================")
        print("Checking:",name)
        print("From",hostname)
        print("==============================================")
        print(hostname,color("--->",fore="green"),name)
        print("==============================================")
    
        def get_status(site):
            time.sleep(delay)
            try:
                response = requests.head(site, timeout=5)
                status_code = response.status_code
                reason = response.reason
            except requests.exceptions.ConnectionError:
                status_code = '000'
                reason = 'ConnectionError'
            website_status = WebsiteStatus(status_code, reason)
            return website_status

        for i in range(tryn):
            site = name
            website_status = get_status(site)
            print("{0:30} {1:10} {2:10}"
                .format(site, website_status.status_code, website_status.reason))

    if ipxcommand == "isup -s":
        import requests
        from collections import namedtuple
        import time
        WebsiteStatus = namedtuple('WebsiteStatus', ['status_code', 'reason'])
        name = input("HTTP Domain>")
        print("[OUT]")
        try:
            response = requests.head(name, timeout=5)
            status_code = response.status_code
            reason = response.reason
        except requests.exceptions.ConnectionError:
            status_code = '000'
            reason = 'ConnectionError'
        website_status = WebsiteStatus(status_code, reason)

        print("The server",name,"is",reason)

    if ipxcommand == "whois":
        from ipwhois import IPWhois

        import pprint

        obj = IPWhois(input("IP>"))
        import itertools
        import threading
        import time
        import sys
        import os
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rloading: ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\r[OUT]')
        t = threading.Thread(target=animate)
        t.start()
        results = obj.lookup_rdap(depth=1)
        time.sleep(1)
        done = True
        
        print("\n")
        pprint.pp(results)
      
    if ipxcommand == "os":
        print(platform.system())
    
    if ipxcommand == "cpu":
        print(platform.processor())

    if ipxcommand == "ver":
        print(platform.version())

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
12|htmlrip    |rips html off websites    
13|isup       |checks if a domain is up
14|isup -s    |checks if a domain is up ina nicer veiw
15|whois      |find out who's who with an ip
16|os         |find out what os type you have
17|cpu        |find out what cpu type you have
18|ver        |Returns the system's release version
19|filefind   |Returns a url where a extention is of your choice
=======================================================
        """)
