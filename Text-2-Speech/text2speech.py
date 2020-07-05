# Import the required module for text
# to speech conversion
from gtts import gTTS
import os
import urllib.request, urllib.error, urllib.parse
import datetime
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

now = datetime.datetime.now()
print("Current Time:", now)
now = str(now)
filename = now[:4] + "_" + now[5:7] + "_" + now[8:10] + "__" + now[11:13] + "_" + now[14:16] + "_" + now[17:19]
print(filename)

mytext = ' Hey, Tejas this side, what about you.'

url = input("Enter URL - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
#print(text)

#handle = open(filename + ".mp3", "w+")
#handle.write(text)
#handle.close()

myNews = gTTS(text=text, lang="en", slow=False)
myNews.save(filename + ".mp3")
print("saving player ....")
os.system(filename + ".mp3")

print("starting player ....")

