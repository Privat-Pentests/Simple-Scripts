import requests
import sys
import os
import time

domain = sys.argv[1]
file = open("{}//subdomains.txt".format(os.path.dirname(__file__)))
subdomains = []

if __name__ == '__main__':
    startTime = round(time.time() * 1000)
    found = []

    if len(sys.argv) > 1:
        for i in file.readlines():
            subdomains.append(i.replace("\n", ""))

        print("Checking {} Subdomains of {}...".format(len(subdomains), domain))

        for subdomain in subdomains:
            url = 'http://{}.{}'.format(subdomain, domain)

            try:
                requests.get(url)
            except:
                pass
            else:
                found.append(subdomain)
                print('Found: {}'.format(subdomain, domain))

        print("Founded {} Subdomains of {} in {}ms.".format(len(found), domain, round(time.time() * 1000) - startTime))
    else:
        print("Please enter a domain.")
        pass
