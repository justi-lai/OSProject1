# OSProject1
CS 4348.502 Project 1 - Logger, Encryption, and Driver programs.

Logger:
    Logs the time and value of every input to the driver program, 
    and any messages sent between driver.py and encryption.py
    The logs are in the following format:
        YYYY-MM-DD HH:MM [ACTION] MESSAGE

Encryption:
    Performs all of the encryption and decryption of strings.
    The current passkey is stored in this process.
    The input is recieved from driver.py, and outputted 
    back to driver.py

Driver:
    Interacts with the user and stores the history.
    Driver also runs the logger and encryption 
    subprocesses and communicates and connects the two for 
    one application experience for both encryption and
    logging.

HOW TO RUN:
    This code is written for python3, therefore it may differ between OS

    Run the current directory where these files are stored at in terminal (cmd)
    Then type in the following command based on your OS

    WINDOWS:
        py ./driver.py {your log file name}
    
    MACOS:
        python3 ./driver.py {your log file name}
    
    LINUX:
        python3 ./driver.py {your log file name}

    CS1 Machines:
        python3 ./driver.py {your log file name}

TA NOTES:
    This project was written in python3 version 3.12.7, but I have tried to make it work on the CS machines.
    There is no guarentee that it will work on the CS machines as I have not tested that, but this should be 
    version 3.6 compatible. It is still very much prefered for this program to be run on your native device
    running python 3.12 as this is proven to work on my machine.

    Another note is that in the log file, there will be some logs that show [INPUT] and then a number. This
    is intended as the user will be inputting a number as an input.

    Thank you!