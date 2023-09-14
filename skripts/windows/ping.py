import os

while True:
    stream = os.popen('ping www.google.com')
    output = stream.read()
    print(output)
    if output != 'Ping request could not find host www.google.com. Please check the name and try again.\n':
        break