#obj: creer une copie d'une clef usb donc recupere les fichiers d'une clef usb et les copie dans un dossier de destination
import os
import subprocess
import psutil
import pyusb
import time

def detecter_cle_usb():
    while True:
        time.sleep(5)
        cmd_pour_check= subprocess.run("Get-WmiObject -Class Win32_LogicalDisk", shell=True)
        if cmd_pour_check.returncode != 0:
            print("Clé USB détectée !")
            print(cmd_pour_check)
        else:
            print("Aucune clé USB détectée.")
        pass
