import sys

def output(action='RESULT', message=''):
    if message != '':
        result = f'{action} {message}'
        print(result)
    else:
        print(action)
    sys.stdout.flush()

def main():
    passkey = ''
    while True:
        log = sys.stdin.readline().rstrip()
        log_parts = log.split(maxsplit=1)
        action = log_parts[0].upper()
        if action == 'QUIT':
            break
        message = log_parts[1] if len(log_parts) > 1 else ''

        if action == 'PASSKEY':
            passkey = message
            print('e test')
            output()
            print('encryption test')
        # elif action == 'ENCRYPT':
        #     body
        # elif action == 'DECRYPT':
        #     body
        else:
            print('Error: Invalid Input')

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('ERROR: incorrect usage of encryption')
        sys.exit(1)
    print('encryption running')
    #print(sys.stdin.readline())
    main()