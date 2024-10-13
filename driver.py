import subprocess
import sys

def startProcesses(logFile):
    loggerProcess = subprocess.Popen(
        ['py', './logger.py', logFile],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf8'
    )
    encryptionProcess = subprocess.Popen(
        ['py', './encryption.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf8'
    )
    return loggerProcess, encryptionProcess

def logMessage(process, action, message=''):
    process.stdin.write(f'{action} {message}\n')
    process.stdin.flush()

def processEncryption(text):
    log = text.split(maxsplit=1)
    action = log[0]
    message = ''
    if len(log) > 1:
        message = log[1]
    return action, message

def menu():
    print('\n***************')
    print('\nMenu')
    print('1. PASSWORD')
    print('2. ENCRYPT')
    print('3. DECRYPT')
    print('4. HISTORY')
    print('5. QUIT')

def password(logger, encryption, history):
    logMessage(logger, 'INPUT', 'PASSWORD')

    word = ''
    while True:
        print('\nPASSWORD')
        print('1. NEW PASSWORD')
        print('2. HISTORY')
        print('3. BACK')
        command = input('INPUT: ').rstrip().upper()
        if command == '1' or command == 'NEW' or command == 'NEW PASSWORD':
            logMessage(logger, 'INPUT', 'NEW PASSWORD')
            word = input('NEW PASSWORD: ')
            history.append(word)
            break

        elif command == '2' or command == 'HISTORY':
            logMessage(logger, 'INPUT', 'HISTORY')
            if len(history) == 0:
                print('No available passwords.')
                logMessage(logger, 'ERROR', 'Empty history')
                return
            print('Choose a password:')
            for i in range(1, len(history)+1):
                print(f'{i}. {history[i-1]}')
            print(f'{len(history) + 1}. GO BACK')
            command = input('INPUT: ').rstrip()
            logMessage(logger, 'INPUT', command)
            if command != str(len(history) + 1) and command != 'GO BACK':
                try:
                    word = history[int(command)-1]
                    break
                except:
                    print('Please input a valid number.')
                    logMessage(logger, 'ERROR', 'Invalid input')
            else:
                logMessage(logger, 'INPUT', 'GO BACK')

        elif command == '3' or command == 'BACK':
            logMessage(logger, 'INPUT', 'BACK')
            return

        else:
            print('Please submit a valid input.\n')
            logMessage(logger, 'ERROR', 'Invalid input')
    
    encryption.stdin.write(f'PASSKEY {word}\n')
    encryption.stdin.flush()
    logMessage(logger, 'PASSKEY', word)
    result, message = processEncryption(encryption.stdout.readline().rstrip())
    logMessage(logger, result, message)
    if result == 'ERROR ':
        print('Error setting password')
    else:
        print('Password set successfully')
        if history.count(word) == 0:
            history.append(word)
    
def encrypt(logger, encryption, history):
    logMessage(logger, 'INPUT', 'ENCRYPT')

    word = ''
    while True:
        print('\nENCRYPT')
        print('1. NEW STRING')
        print('2. HISTORY')
        print('3. BACK')
        command = input('INPUT: ').rstrip().upper()
        if command == '1' or command == 'NEW' or command == 'NEW STRING':
            logMessage(logger, 'INPUT', 'NEW STRING')
            word = input('NEW STRING: ')
            history.append(word)
            break

        elif command == '2' or command == 'HISTORY':
            logMessage(logger, 'INPUT', 'HISTORY')
            if len(history) == 0:
                print('No available strings.')
                logMessage(logger, 'ERROR', 'Empty history')
                return
            print('Choose a string:')
            for i in range(1, len(history)+1):
                print(f'{i}. {history[i-1]}')
            print(f'{len(history) + 1}. GO BACK')
            command = input('INPUT: ').rstrip()
            logMessage(logger, 'INPUT', command)
            if command != str(len(history) + 1) and command != 'GO BACK':
                try:
                    word = history[int(command)-1]
                    break
                except:
                    print('Please input a valid number.')
                    logMessage(logger, 'ERROR', 'Invalid input')
            else:
                logMessage(logger, 'INPUT', 'GO BACK')

        elif command == '3' or command == 'BACK':
            logMessage(logger, 'INPUT', 'BACK')
            return
        
        else:
            print('Please submit a valid input.\n')
            logMessage(logger, 'ERROR', 'Invalid input')

    encryption.stdin.write(f'ENCRYPT {word}\n')
    encryption.stdin.flush()
    logMessage(logger, 'ENCRYPT', word)
    result, message = processEncryption(encryption.stdout.readline().rstrip())
    logMessage(logger, result, message)
    if result == 'ERROR ':
        print(message)
    else:
        print(f'{result}: {message}')
        if history.count(message) == 0:
            history.append(message)


def decrypt(logger, encryption, history):
    logMessage(logger, 'INPUT', 'DECRYPT')

    word = ''
    while True:
        print('\nDECRYPT')
        print('1. NEW STRING')
        print('2. HISTORY')
        print('3. BACK')
        command = input('INPUT: ').rstrip().upper()
        if command == '1' or command == 'NEW' or command == 'NEW STRING':
            logMessage(logger, 'INPUT', 'NEW STRING')
            word = input('NEW STRING: ')
            history.append(word)
            break

        elif command == '2' or command == 'HISTORY':
            logMessage(logger, 'INPUT', 'HISTORY')
            if len(history) == 0:
                print('No available strings.')
                logMessage(logger, 'ERROR', 'Empty history')
                return
            print('Choose a string:')
            for i in range(1, len(history)+1):
                print(f'{i}. {history[i-1]}')
            print(f'{len(history) + 1}. GO BACK')
            command = input('INPUT: ').rstrip()
            logMessage(logger, 'INPUT', command)
            if command != str(len(history) + 1) and command != 'GO BACK':
                try:
                    word = history[int(command)-1]
                    break
                except:
                    print('Please input a valid number.')
                    logMessage(logger, 'ERROR', 'Invalid input')
            else:
                logMessage(logger, 'INPUT', 'GO BACK')
        
        elif command == '3' or command == 'BACK':
            logMessage(logger, 'INPUT', 'BACK')
            return
        
        else:
            print('Please submit a valid input.\n')
            logMessage(logger, 'ERROR', 'Invalid input')

    encryption.stdin.write(f'DECRYPT {word}\n')
    encryption.stdin.flush()
    logMessage(logger, 'DECRYPT', word)
    result, message = processEncryption(encryption.stdout.readline().rstrip())
    logMessage(logger, result, message)
    if result == 'ERROR ':
        print(message)
    else:
        print(f'{result}: {message}')
        if history.count(message) == 0:
            history.append(message)


def history(logger, history):
    logMessage(logger, 'INPUT', 'HISTORY')

    if len(history) == 0:
        print('No available strings.')
        logMessage(logger, 'ERROR', 'Empty history')
        return
    for i in range(1, len(history)+1):
        print(f'{i}. {history[i-1]}')
    input('Enter any key to return...')


def main(logFile):
    logger, encryption = startProcesses(logFile)

    history_list = []

    menu()
    command = input('INPUT: ').strip().upper()
    while command != '5' and command != 'QUIT':
        if command == '1' or command == 'PASSWORD':
            password(logger, encryption, history_list)
        elif command == '2' or command == 'ENCRYPT':
            encrypt(logger, encryption, history_list)
        elif command == '3' or command == 'DECRYPT':
            decrypt(logger, encryption, history_list)
        elif command == '4' or command == 'HISTORY':
            history(logger, history_list)
        else:
            print('ERROR: Unknown input. Please try again.')
        menu()
        command = input('INPUT: ').strip().upper()
    
    logMessage(logger, 'QUIT')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    main(log_file)