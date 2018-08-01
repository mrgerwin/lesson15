from guizero import App, TextBox, PushButton, yesno, MenuBar, warn
from tkinter import filedialog
from random import randint
   
def openFile():
    global data
    app.filename=filedialog.askopenfilename(initialdir="/", title="Open", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    #print(app.filename)                                                                                              
    theFile = open(app.filename, "r")
    data.value=theFile.read()
    app.title = app.filename
    theFile.close()
    
def saveFile():
    global data
    app.filename=filedialog.asksaveasfilename(initialdir="/", title="Save as", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    theFile = open(app.filename, "w")
    theFile.write(data.value)
    app.title = app.filename
    theFile.close()
    
def encryptFile():
    global data, otpfilename
    if len(otpfilename)>0:
        warn("Encryption", "Data Encrypted Using " + otpfilename)
        data.value = encrypt(data.value, load_sheet(otpfilename))
    else:
        warn("Encryption", "No OTP file loaded so not Encrypted")

def encrypt(plaintext, sheet):
    global ALPHABET
    ciphertext=''
    for position, character in enumerate(plaintext):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) + int(sheet[position]))%26
            ciphertext += ALPHABET[encrypted]
    return ciphertext

def decrypt(ciphertext, sheet):
    global ALPHABET
    plaintext = ''
    for position, character in enumerate(ciphertext):
        if character not in ALPHABET:
            plaintext += character
        else:
            decrypted = (ALPHABET.index(character)-int(sheet[position]))%26
            plaintext += ALPHABET[decrypted]
    return plaintext
    
def decryptFile():
    global data, otpfilename
    if len(otpfilename)>0:
        sheet = load_sheet(otpfilename)
        data.value = decrypt(data.value, sheet)
        warn("Decrypt", "Data Decrypted using key " + otpfilename)
    else:
        warn("Decrypt", "No OTP file loaded so not decrypted")

def get_plain_text():
    global data
    plain_text = data.value
    return plain_text.lower()

def generate_otp(sheets, length):
    for sheet in range(sheets):
        with open("otp" + str(sheet) + ".txt", "w") as f:
            for i in range(length):
                f.write(str(randint(0,26))+"\n")

def load_sheet(filename):
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents

def OTPHandler():
    global data
    length = len(data.value)
    generate_otp(1, length)
    warn("OTP", "Made 1 OTP Key of Length " + str(length))

def SetOTPHandler():
    global otpfilename
    otpfilename = filedialog.askopenfilename(title="Open OTP", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    warn("OTP", "Using OTP " + otpfilename)
    
def closeHandler():
    if yesno("close", "Do you want to quit without saving?"):
        app.destroy()

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
app = App(title="untitled", height=600, width=600)
data = TextBox(app, height=600, width=600, multiline=True, scrollbar=True)
otpfilename = ""
menubar = MenuBar(app, toplevel = ["File", "Encrypt"],
                  options=[
                      [["Open File", openFile], ["Save File", saveFile]],
                      [["Encrypt", encryptFile], ["Decrypt", decryptFile], ["Make OTP", OTPHandler], ["Set OTP", SetOTPHandler]]
                    ])
app.on_close(closeHandler)
app.display()