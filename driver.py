import subprocess
import os
import sys

def startProcesses(logFile):
    loggerProcess = subprocess.Popen(
        ['python3', './logger.py', logFile],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    encryptionProcess = subprocess.Popen(
        ['python3', './encryption.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    # loutput, lerrors = loggerProcess.communicate()
    # eoutput, eerrors = encryptionProcess.communicate()
    # print(loutput)
    # print(eoutput)

def main(logFile):
    startProcesses(logFile)

if __name__ == 'main':
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    main(log_file)