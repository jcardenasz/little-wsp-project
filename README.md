To execute this project you have to:

1. Have Python installed on your machine. You can download it [here](https://www.python.org/downloads/).
2. Clone this repository to your machine.
3. Install the required libraries by running the following command in the terminal:
```bash
pip install -r requirements.txt
```
4. Create a .env file and add the following variables:
```bash
# The phone number you want to send the message to replaces the x's
PHONENUMBER = +XXXXXXXXXXXX

# The message you want to send
MESSAGE = This is a test message
```
5. Remember to change the arguments A and B in the function sendwhatmsg: 
```bash
pywhatkit.sendwhatmsg(str(phonenum), str(message), A, B)
```
These arguments are A: hour, B: minute when the message is going to be sended.
6. Run the script by clicking the run button or by running the following command in the terminal inside the root dir:
```bash
python main.py
```

Juan Camilo Cárdenas Zabala, Software developer
[jcardenasz@unal.edu.co](https://www.linkedin.com/in/juan-camilo-c%C3%A1rdenas-zabala-5aa65b309/).
