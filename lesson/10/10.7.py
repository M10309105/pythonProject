#/usr/bin/python3
#
#Class
print("=" * 100)
print("10.7 Internet Access")
print("=" * 100)

#urllib.requests
#smtplib
from urllib.request import urlopen

with urlopen('https://tinyurl.com/yvtzcthz') as response:
    for line in response:
        print(line.decode('utf-8'))
    
import smtplib
# server = smtplib.SMPT('localhost')
# server.sendmail('someone@localhost.com', 'somebody@remote.com',
# """TO: somebody@remote.com
# From: someone@localhost.com

# This is content
# """)
# server.quit()
