# BEMANIWIKI SDVX SKILL ANALYZER

A fork of bemaniwiki SDVX skill analyzer pages' wiki source codes. 

- VIVID WAVE: http://bemaniwiki.com/index.php?SOUND%20VOLTEX%20VIVID%20WAVE/SKILL%20ANALYZER

- EXCEED GEAR: http://bemaniwiki.com/index.php?SOUND%20VOLTEX%20EXCEED%20GEAR/SKILL%20ANALYZER

## Github Actions

Run crawler.py every Monday (UTC 00:00) and update the wiki source codes.

## Repo Structure

### wiki_source/...

The wiki source codes of corresponding pages.

### crawler.py

Usage: `python3 crawler.py`.

A python crawler script to crawl skill analyzer wiki source codes into text files under `wiki_source` directory. Now support **VIVID WAVE** and **EXCEED GEAR**.

### gen_wiki.py[DEPRECATED]

Usage: `python3 gen_wiki.py filename`.

A python script to generate skill analyzer courses wiki source codes.
