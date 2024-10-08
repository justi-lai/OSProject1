import sys
import datetime

def write(log_file, action, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"{timestamp} [{action}] {message}"
    with open(log_file, mode='a') as file:
        file.write(entry + '\n')

def process_log(log_file):
    while True:
        log = sys.stdin.readline().rstrip()
        log_parts = log.split(maxsplit=1)
        action = log_parts[0].upper()
        if action == 'QUIT':
            write(log_file, action, '')
            break
        message = log_parts[1] if len(log_parts) > 1 else ''

        write(log_file, action, message)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('ERROR: incorrect usage | Usage: py logger.py <log_file>')
        sys.exit(1)
   # print('logger running')
    LOG_FILE = sys.argv[1]
    write(LOG_FILE, 'START', 'Logging Started.')
    process_log(LOG_FILE)