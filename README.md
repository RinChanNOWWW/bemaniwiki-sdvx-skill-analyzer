# BEMANIWIKI SDVX VIVID WAVE SKILL ANALYZER

A fork of bemaniwiki SDVXV skill analyzer page's wiki source codes. http://bemaniwiki.com/index.php?SOUND%20VOLTEX%20VIVID%20WAVE/SKILL%20ANALYZER

## Github Actions

Run crawler.py every Monday (UTC 00:00) and update this repo.

## Repo Structure

### content.txt

The wiki source of this page.

### gen_wiki.py

Usage: `python3 gen_wiki.py filename`.

A python script to generate skill analyzer courses wiki source codes.

### crawler.py

Usage: `python3 crawler.py`.

A python crawler script to crawl skill analyzer wiki source codes into `context.txt`.

### courses

Texts for `gen_wiki.py` to generate codes.

Content example:

```
01|Triple Counter|EXH|17
02|The world of sound|EXH|17
FINAL|ほおずき程度には赤い頭髪|EXH|17
```

### wiki

The results of `gen_wiki.py`. Follow the wiki rules of http://bemaniwiki.com/index.php?SOUND%20VOLTEX%20VIVID%20WAVE/SKILL%20ANALYZER.

Content example:

```
|01|Triple Counter|BGCOLOR(#f33):EXH|BGCOLOR(#fdd):17|
|02|The world of sound|BGCOLOR(#f33):EXH|BGCOLOR(#fdd):17|
|FINAL|ほおずき程度には赤い頭髪|BGCOLOR(#f33):EXH|BGCOLOR(#fdd):17|
```

