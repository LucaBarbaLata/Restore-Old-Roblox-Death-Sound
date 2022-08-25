import requests
import urllib.request
import os 
from shutil import copyfile

urllib.request.urlretrieve("https://github.com/LucaBarbaLata/Restore-Old-Roblox-Death-Sound/raw/main/Roblox-Death-Sound-Sound-Effect-_HD_.ogg","ouch.ogg")
username = os.getlogin()

os.remove(f"C:\\Users\\{username}\\AppData\\Local\\Roblox\\Versions\\version-c9e77bcac5104752\\content\\sounds\\ouch.ogg")



src= os.path.abspath(os.getcwd()) + "\\ouch.ogg"
dst = f"C:\\Users\\{username}\\AppData\\Local\\Roblox\\Versions\\version-c9e77bcac5104752\\content\\sounds\\ouch.ogg"
copyfile(src, dst)

