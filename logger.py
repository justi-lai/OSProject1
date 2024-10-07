import sys
import datetime

def write(log_file, action, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"{timestamp} [{action}] {message}"
    with open(log_file, mode='w') as file:
        file.write(entry + '\n')

def process_log(log_file):
    while True:
        log = sys.stdin.readline().rstrip()

        if log == 'QUIT':
            break

        log_parts = log.split(maxsplit=1)
        action = log_parts[0]
        message = log_parts[1] if len(log_parts) > 1 else ''

        write(log_file, action, message)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('ERROR: incorrect usage | Usage: py logger.py <log_file>')
        sys.exit(1)
    
    LOG_FILE = sys.argv[1]
    process_log(LOG_FILE)