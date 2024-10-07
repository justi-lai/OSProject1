import subprocess
import os
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

def logMessage(process, message):
    process.stdin.write(message + '\n')


def main(logFile):
    logger, encryption = startProcesses(logFile)
    lout, lerr = logger.communicate()
    eout, eerr = encryption.communicate()
    print(lout, eout)

if __name__ == '__main__':
    print('running')
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    main(log_file)