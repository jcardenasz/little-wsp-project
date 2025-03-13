import pywhatkit, os, pyautogui
from dotenv import load_dotenv
import time

#environment variables load
load_dotenv()

#env variables loaded into usable variables
phonenum = os.getenv('PHONENUMBER')
message = os.getenv('MESSAGE')

#sending message to requested phonenumber
pywhatkit.sendwhatmsg(str(phonenum),str(message),19,57)

#waiting for whatsapp tab to be opened and message written
time.sleep(15)

#changing tabs in order to send the message properly
pyautogui.hotkey("alt", "tab")

#message send command
time.sleep(3)
pyautogui.press("enter")









