from os import error
from typing import cast
import requests
import re


def run_crawler(url, target_file):
    try:
        r = requests.get(url)
        contents = re.findall(
            r'<textarea name="msg" rows="20" cols="80">(.+?)</textarea>', r.text, re.S)
        content = contents[0]
        file = open('wiki_source/{}'.format(target_file), 'w')
        file.write(content)
    except error:
        print("curl {} skill analyzer failed: {}", target_file, error.strerror)


run_crawler(
    'https://bemaniwiki.com/index.php?cmd=edit&page=SOUND%20VOLTEX%20VIVID%20WAVE/SKILL%20ANALYZER', "vivid wave")

run_crawler(
    'http://bemaniwiki.com/index.php?cmd=edit&page=SOUND%20VOLTEX%20EXCEED%20GEAR/SKILL%20ANALYZER', 'exceed gear')
