# lesson15
Finish the Encryption App

1. Using the finished app wordproccessor0-4, change your app so that it will make and load a OTP.
2. Use the App to encrypt a file that is several lines long.
3. Use the app to encrypt a file that is atleast 500 characters long.
4. Swap your files and associated OTP files with another student.
5. Use your app to decrypt their files using the encrypted file and associated OPT files

### Discussion Questions  
*In this section respond to the questions based upon the drawbacks brought up at the end of the Secret Agent Chat lesson.*

**While a one-time pad offers perfect secrecy, you still have to be careful if you want to remain really secure, and there are some issues with this program.**  
* To send encrypted messages to each other, you can use email, SMS or even social media such as Facebook or Twitter. It won’t even matter if your posts are public, as the only person who could decrypt the message is your friend.
1. What is the piece of information that cannot be public in order for this system to work?
* Once you’ve generated your OTP, such as by generating 100 sheets, you need to transfer them to the person you want to communicate with. You can’t send them electronically, such as by email, as this is insecure. Probably the most secure method is giving them to your friend on a storage device, such as an SD card or USB flash memory.
2. Why do you think that it is difficult to use this way of encryption in the real-world?
* The OTP method is only secure if you and your friend keep the OTP secure.
3. Some programs will retrieve files even after they have been deleted.  How would this affect the sense of security that you get from the one-time key method?
* The OTP relies on the randomness of the random number generator. If the generator isn’t truly random, then the OTP could be cracked. Python’s random module is probably not the best way of generating random numbers.
4. Explain what you think this bullet point mean.
* Your message can’t be longer than the length of the sheet from the OTP. If you’re not sure how long your messages will be, it’s better to generate large sheets just in case.
5. We live in an age where file size is not usually a problem but, what if it is?  Explain the disadvantage that this method might have now that you understand the size of the OTP.

