#obj: creer une copie d'une clef usb donc recupere les fichiers d'une clef usb et les copie dans un dossier de destination
import os
import subprocess
import shutil
import pandas
#import pyusb
import time

def detecter_cle_usb():
    while True:
        time.sleep(5)
        cmd_pour_check= subprocess.run(["powershell", "-Command", "Get-WmiObject -Class Win32_LogicalDisk"], shell=True, capture_output=True, text=True)
        if cmd_pour_check.returncode == 0:
            print("Clé USB détectée !")
            print(cmd_pour_check.stdout)
        else:
            print("Aucune clé USB détectée.")

def copier_fichiers_cle_usb(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    for root, dirs, files in os.walk(source):
        rel_path = os.path.relpath(root, source)
        dest_dir = os.path.join(destination, rel_path)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        for file in files:
            src_file = os.path.join(root, file)
            road_file = os.path.abspath(src_file)
            dest_file = os.path.join(dest_dir, file)
            try:
                shutil.copy2(src_file, dest_file)
                print(f"Fichier {src_file} copié avec succès dans {dest_file}")
                print(f"le chemin du fichier en cours de copie est : {road_file}")
                shutil.make_archive(dest_file, 'zip', dest_dir)
                print(f"Fichier {dest_file} compressé en {dest_file}.zip")
            except Exception as e:
                print(f"Erreur lors de la copie de {src_file} : {e}")

if __name__ == "__main__":
    print("Détection de la clé USB en cours...")
    #detecter_cle_usb()
    source = input("Entrez le chemin de la clé USB (ex: E:\\) : ")
    destination = input("Entrez le chemin du dossier de destination (ex: C:\\copie_cle_usb) : ")
    copier_fichiers_cle_usb(source, destination)