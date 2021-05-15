import requests
import sys
import os

domain = sys.argv[1]
file = open("{}//subdomains.txt".format(os.path.dirname(__file__)))
subdomains = []

if __name__ == '__main__':

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
                print('Found: {}'.format(subdomain, domain))
    else:
        print("Please enter a domain.")
        pass
