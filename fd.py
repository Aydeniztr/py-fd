import wget
banner = '''
██╗    ██╗███████╗██████╗  ██████╗ ███████╗████████╗
██║    ██║██╔════╝██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝
██║ █╗ ██║█████╗  ██████╔╝██║  ███╗█████╗     ██║   
██║███╗██║██╔══╝  ██╔══██╗██║   ██║██╔══╝     ██║   
╚███╔███╔╝███████╗██████╔╝╚██████╔╝███████╗   ██║   
 ╚══╝╚══╝ ╚══════╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   
                                                    
'''

print(banner)
    
url = input(str('\n[?] put the file link you want to download\n └>'))

directory_name = input(str('\n[?] select a directory to save the file\n └>'))

wait = input('\n[+]Enter to continue…')

filename = wget.download(url,out = directory_name)

print ( '\n[!] file saved succsesfully to %s !' % directory_name)

