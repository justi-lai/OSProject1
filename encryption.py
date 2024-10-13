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
            passkey = message.upper()
            output('RESULT', '')
        
        elif action == 'ENCRYPT':
            if passkey == '':
                output('ERROR', 'Password not set')
            else:
                result = ''
                key_idx = 0
                for character in message:
                    if character.isalpha():
                        char_code = ''
                        if character.isupper():
                            char_code = ord(character) - ord('A')
                        else:
                            char_code = ord(character) - ord('a')
                        key_code = ord(passkey[key_idx % len(passkey)])
                        shift = key_code - ord('A')

                        encrypted_character = ''
                        if character.isupper():
                            encrypted_character = chr(((char_code + shift) % 26) + ord('A'))
                        else:
                            encrypted_character = chr(((char_code + shift) % 26) + ord('a'))
                        
                        result += encrypted_character
                        key_idx += 1
                    else:
                        result += character
                output(message=result)

        elif action == 'DECRYPT':
            if passkey == '':
                output('ERROR', 'Password not set')
            else:
                result = ''
                key_idx = 0
                for character in message:
                    if character.isalpha():
                        char_code = ''
                        if character.isupper():
                            char_code = ord(character) - ord('A')
                        else:
                            char_code = ord(character) - ord('a')
                        key_code = ord(passkey[key_idx % len(passkey)])
                        shift = key_code - ord('A')

                        encrypted_character = ''
                        if character.isupper():
                            encrypted_character = chr(((char_code - shift) % 26) + ord('A'))
                        else:
                            encrypted_character = chr(((char_code - shift) % 26) + ord('a'))
                        
                        result += encrypted_character
                        key_idx += 1
                    else:
                        result += character
                output(message=result)
        else:
            output('ERROR', 'Unrecognized input')

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('ERROR: incorrect usage of encryption')
        sys.exit(1)
    main()