import re,urllib
import urllib.request
webpage = urllib.request.urlopen('https://www.redbus.my/bus/bus-online-ticket')
content = webpage.read()
print(content)

pattern_contact = re.compile(r'([+](60)(-)?(\d){9})')
contact = pattern_contact.findall(str(content),re.I)

for i in contact:
    print(i[0])