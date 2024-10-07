import subprocess
import sys

def startProcesses(logFile):
    loggerProcess = subprocess.Popen(
        ['py', './logger.py', logFile],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    encryptionProcess = subprocess.Popen(
        ['py', './encryption.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return loggerProcess, encryptionProcess

def logMessage(process, action, message=''):
    process.stdin.write(action + '\n')
    if message != '':
        process.stdin.write(message + '\n')
    process.stdin.flush()

def menu():
    print('\nMenu')
    print('1. PASSWORD')
    print('2. ENCRYPT')
    print('3. DECRYPT')
    print('4. HISTORY')
    print('5. QUIT')

def password():
    # temp

def encrypt():


def decrypt():


def history():


def main(logFile):
    logger, encryption = startProcesses(logFile)
    
    command = input().strip()
    while command is not '5':
        menu()
        if command == 1:
            password()
        elif command == 2:
            encrypt()
        elif command == 3:
            decrypt()
        else:
            history()
    
    logMessage(logger, 'QUIT')
    


if __name__ == '__main__':
    print('running')
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    main(log_file)