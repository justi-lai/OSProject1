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
    process.stdin.write(f'{action} {message}\n')
    process.stdin.flush()

def menu():
    print('\n***************')
    print('\nMenu')
    print('1. PASSWORD')
    print('2. ENCRYPT')
    print('3. DECRYPT')
    print('4. HISTORY')
    print('5. QUIT')

def password(logger, encryption, passwords):
    print('\nPASSWORD')
    print('1. NEW PASSWORD')
    print('2. HISTORY')
    print('3. BACK')

    word = ''
    while True:
        command = input('INPUT: ').rstrip().upper()
        if command == '1' or command == 'NEW' or command == 'NEW PASSWORD':
            logMessage(logger, 'INPUT', 'NEW PASSWORD')
            word = input('NEW PASSWORD: ')
            print('point1')
            passwords.append(word)
            print(passwords)
            break
        elif command == '2' or command == 'HISTORY':
            logMessage(logger, 'INPUT', 'HISTORY')
            if len(passwords) == 0:
                print('No available passwords.')
                return
            print('Choose a password:')
            for i in range(1, len(passwords)+1):
                print(f'{i}. {passwords[i-1]}')
            command = input('INPUT: ').rstrip()
            try:
                word = passwords[int(command)-1]
                break
            except:
                print('Please input a valid number.\n')
        elif command == '3' or command == 'BACK':
            logMessage(logger, 'INPUT', 'BACK')
            return
        else:
            print('Please submit a valid input.\n')
    
    encryption.stdin.write(f'PASSKEY {word}\n')
    encryption.stdin.flush()
    logMessage(logger, 'PASSKEY', word)
    

# def encrypt():


# def decrypt():


# def history():


def main(logFile):
    logger, encryption = startProcesses(logFile)

   # print(encryption.pid)

    # encryption.stdin.write('this is a test')
    # encryption.stdin.flush()
    #print(encryption.stdout.readline())


    passwords = []

    menu()
    command = input('INPUT: ').strip().upper()
    while command != '5' and command != 'QUIT':
        if command == '1' or command == 'PASSWORD':
            logMessage(logger, 'INPUT', 'PASSWORD')
            password(logger, encryption, passwords)
        # elif command == '2' or command == 'ENCRYPT':
        #     encrypt()
        # elif command == '3' or command == 'DECRYPT':
        #     decrypt()
        # elif command == '4' or command == 'HISTORY':
        #     history()
        else:
            print('ERROR: Unknown input. Please try again.')
        menu()
        command = input('INPUT: ').strip().upper()
    
    logMessage(logger, 'QUIT')
    


if __name__ == '__main__':
    #print('running')
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    main(log_file)