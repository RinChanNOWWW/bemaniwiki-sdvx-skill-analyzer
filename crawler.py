import requests
import re

url = 'https://bemaniwiki.com/index.php?cmd=edit&page=SOUND%20VOLTEX%20VIVID%20WAVE/SKILL%20ANALYZER'
r = requests.get(url)
contents = re.findall(r'<textarea name="msg" rows="20" cols="80">(.+?)</textarea>', r.text, re.S)
content = contents[0]
writeFile = open('content.txt', 'w')
writeFile.write(content)