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
    print('\n***************')
    print('\nMenu')
    print('1. PASSWORD')
    print('2. ENCRYPT')
    print('3. DECRYPT')
    print('4. HISTORY')
    print('5. QUIT')

def password(process, passwords):
    print('\nPASSWORD')
    print('1. NEW PASSWORD')
    print('2. HISTORY')
    print('3. BACK')

    password = ''
    while True:
        command = input('INPUT: ').rstrip().upper()
        if command == '1' or command == 'NEW' or command == 'NEW PASSWORD':
            password = input('NEW PASSWORD: ')
            passwords.append(password)
            break
        elif command == '2' or command == 'HISTORY':
            if len(passwords) == 0:
                print('No available passwords.')
                return
            print('Choose a password:')
            for i in range(1, len(passwords)+1):
                print(f'{i}. {passwords[i-1]}')
            command = input('INPUT: ').rstrip()
            try:
                password = passwords[int(command)-1]
            except:
                print('Please input a valid number.\n')
        elif command == '3' or command == 'BACK':
            return
        else:
            print('Please submit a valid input.\n')
        
    process.stdin.write('PASSKEY\n')
    process.stdin.write(password + '\n')
    process.stdin.flush()

# def encrypt():


# def decrypt():


# def history():


def main(logFile):
    logger, encryption = startProcesses(logFile)

    passwords = []

    menu()
    command = input('INPUT: ').strip().upper()
    while command != '5' and command != 'QUIT':
        if command == '1' or command == 'PASSWORD':
            password(encryption, passwords)
        # elif command == '2' or command == 'ENCRYPT':
        #     encrypt()
        # elif command == '3' or command == 'DECRYPT':
        #     decrypt()
        # elif command == '4' or command == 'HISTORY':
        #     history()
        else:
            print('ERROR: Unknown input. Please try again.')
        menu()
        command = input().strip().upper()
    
    logMessage(logger, 'QUIT')
    


if __name__ == '__main__':
    print('running')
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    main(log_file)