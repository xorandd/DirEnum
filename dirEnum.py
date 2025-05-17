import sys
import requests
import threading

def programUsage():
    print("-h,  --help              Print help menu")
    print("-d,  --direnum           Enumerate directories")
    print("-sd, --subenum           Enumerate subdomains")
    print("-u,  --url               Target url")
    print("-w,  --wordlist          Path to wordlist")
    print("-t,  --threads           Number of threads")
    print("------------------------------------------------")
    print("Usage example: ")
    print("python dirEnum.py -d -u http://10.10.10.10/ -w /path/to/wordlist.txt -t 16")

def worker_dirs(url, dirs):
    for dir in dirs:
        full_url = url + dir.strip()
        try:
            response = requests.get(full_url)
            if response.status_code == 200 or response.status_code == 301:
                print(full_url)
        except:
            pass

def enum_dirs(url, wordlist, num_threads):
    threads = []

    with open(wordlist, 'r') as wordlist_file:
        dir_word = wordlist_file.read().splitlines()
    
    thread_process_amount = max(1, len(dir_word) // num_threads)
    
    for i in range(num_threads):
        start_point = i * thread_process_amount
        end_point = start_point + thread_process_amount
        dir = dir_word[start_point:end_point]

        if not dir:
            break

        thread = threading.Thread(target=worker_dirs, args = (url, dir))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def worker_subdomains(url, subdomains):
    base_url = ""
    protocol = ""

    if url.startswith("http://"):
        protocol = "http://"
        base_url = url[7:]
    elif url.startswith("https://"):
        protocol = "https://"
        base_url = url[8:]
    
    for subdomain in subdomains:
        full_url = protocol + subdomain.strip() + "." + base_url
        try:
            response = requests.get(full_url)
            if response.status_code == 200 or response.status_code == 301:
                print(full_url)
        except requests.exceptions.RequestException:
                pass

def enum_subdomains(url, wordlist, num_threads):
    threads = []
    with open(wordlist, 'r') as wordlist_file:
    #full_url = f"{protocol}{subdomain}.{base_url}"
        subdomain_word = wordlist_file.read().splitlines()        
        
    thread_process_amount = max(1, len(subdomain_word) // num_threads)
    
    for i in range(num_threads):
        start_point = i * thread_process_amount
        end_point = start_point + thread_process_amount
        subdomain = subdomain_word[start_point:end_point]

        if not subdomain:
            break

        thread = threading.Thread(target=worker_subdomains, args = (url, subdomain))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def main():
    if '-h' in sys.argv or "--help" in sys.argv:
        programUsage()
        sys.exit(1)

    if len(sys.argv) < 6:
        print("Some arguments are missing")
        programUsage()
        sys.exit(1)
    
    url = ""
    wordlist = ""
    isDirEnum = False
    isSubEnum = False
    num_threads = 0

    for i in range(1, len(sys.argv)):
        if sys.argv[i] in ['-d', "--direnum"]:
            isDirEnum = True
        elif sys.argv[i] in ['-sd', "--subenum"]:
            isSubEnum = True
        elif sys.argv[i] in ['-u', "--url"]:
            url = sys.argv[i+1]
        elif sys.argv[i] in ['-w', "--wordlist"]:
            wordlist = sys.argv[i+1]
        elif sys.argv[i] in ['-t', "--threads"]:
            num_threads = int(sys.argv[i+1])

    if not url or not wordlist:
        print("Target URL or wordlist are missing")
        programUsage()
        sys.exit(1)
    
    if not url.endswith('/'):
        url += '/'

    if num_threads <= 0:
        num_threads = 10 #by default

    if isDirEnum:
        print("[*] Starting directory enumeration\n")
        enum_dirs(url, wordlist, num_threads)
    if isSubEnum:
        print("[*] Starting subdomain enumeration\n")
        enum_subdomains(url, wordlist, num_threads)
    

if __name__ == "__main__":
    main()
