# DirEnum
Directory/subdomain enumerator

A script that helps you find directories and subdomains of a website using a wordlist

## Features:

- Directory enumeration

- Subdomain enumeration

- -Threading

## How to Use
```
python dirEnum.py -d -u http://target-website.com/ -w /path/to/wordlist.txt -t 20
```
Threading option is optional, 10 by default

You can also enumerate subdomains like this
```
python dirEnum.py -sd -u http://example.com -w /path/to/wordlist.txt
```

## Options

- -h, --help
  - show help menu
- -d,	--direnum
  - directory enumeration
- -sd, --subenum
  - subdomain enumeration
- -u, --url
  - target URL
- -w, wordlist /path/to/wordlist.txt
  - path to wordlist
- -t, --threads <int>
  - Number of threads

## Requirements

- `Python 3.x`
- `requests library`

Install requests library:
```
pip install requests
```
