# DirEnum
Directory/subdomain enumerator

A script that helps you find directories and subdomains of a website using a wordlist

## Features:

- Directory enumeration (-d)

- Subdomain enumeration (-sd)

## How to Use
```
python dirEnum.py -d -u http://target-website.com/ -w /path/to/wordlist.txt
```

You can also enumerate subdomains like this
```
python dirEnum.py -sd -u http://example.com -w /path/to/wordlist.txt
```

## Options

- -h, --help	show help menu
- -d	directory enumeration
- -sd	subdomain enumeration
- -u	target URL
- -w	path to wordlist

## Requirements

- `Python 3.x`
- `requests library`

Install requests library:
```
pip install requests
```
