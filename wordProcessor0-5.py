from guizero import App, TextBox, PushButton, yesno, MenuBar, warn
from tkinter import filedialog
from random import randint
   
def openFile():
    """
    Opens user specified file
    Updates the textbox widget so that it displays the file
    """
    global data
    app.filename=filedialog.askopenfilename(initialdir="/", title="Open", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    #print(app.filename)                                                                                              
    theFile = open(app.filename, "r")
    data.value=theFile.read()
    app.title = app.filename
    theFile.close()
    
def saveFile():
    """
    Saves the textbox value to a filename of the users choice
    """
    global data
    app.filename=filedialog.asksaveasfilename(initialdir="/", title="Save as", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    theFile = open(app.filename, "w")
    theFile.write(data.value)
    app.title = app.filename
    theFile.close()
    
def encryptFile():
    """
    takes the otpfilename and uses load_sheet to open the correct OTP
    Then replaces the value of the textbox widget to the cyphertext
    """
    global data, otpfilename
    if len(otpfilename)>0:
        warn("Encryption", "Data Encrypted Using " + otpfilename)
        data.value = encrypt(data.value, load_sheet(otpfilename))
    else:
        warn("Encryption", "No OTP file loaded so not Encrypted")

def encrypt(plaintext, sheet):
    """
    An encryption algorithm that takes a one time pad and
    generates a shifted alphabet encryption for each letter in the textbox widget
    """
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
    """
    An decryption algorithm that takes a one time pad and
    gets the correct shifted amount for each letter in the textbox widget to return
    the plaintext.
    """
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
    """
    An event handler that manages a decryption
    """
    global data, otpfilename
    if len(otpfilename)>0:
        sheet = load_sheet(otpfilename)
        data.value = decrypt(data.value, sheet)
        warn("Decrypt", "Data Decrypted using key " + otpfilename)
    else:
        warn("Decrypt", "No OTP file loaded so not decrypted")

def get_plain_text():
    """
    A helper function that will translate all letters from the textbox to
    lowercase since the encryption algorithm can only handle lowercase.
    """
    global data
    plain_text = data.value
    return plain_text.lower()

def generate_otp(sheets, length):
    """
    An algorithm that will make the correct sized OTP for the file that needs
    encrypted.
    """
    global otpfilename
    otpfilename=filedialog.asksaveasfilename(title="Save OTP as", filetypes=(("text files", "*.txt"), ("all files", "*.*")))                                                                                              
    theFile = open(otpfilename, "w")
    for i in range(length):
        theFile.write(str(randint(0,26))+"\n")
    theFile.close()

def load_sheet(filename):
    """
    Reads the one time pad into memory and returns it as a list
    """
    with open(filename, "r") as f:
        contents = f.read().splitlines()
    return contents

def OTPHandler():
    """
    A handler for generating the OTP
    """
    global data
    length = len(data.value)
    generate_otp(1, length)
    warn("OTP", "Made 1 OTP Key of Length " + str(length))

def SetOTPHandler():
    """
    A handler for telling the app which OTP to use
    """
    global otpfilename
    otpfilename = filedialog.askopenfilename(title="Open OTP", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    warn("OTP", "Using OTP " + otpfilename)
    
def closeHandler():
    """
    Handles the close event
    """
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