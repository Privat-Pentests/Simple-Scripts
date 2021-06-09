import requests
import json

if __name__ == "__main__":
    domain = input("Which domain do you want to read information from? ")
    request = requests.get("http://ip-api.com/json/{}".format(domain))
    response = json.loads(json.dumps(request.json()))

    if response['status'] != 'success':
        print("No information could be found for this domain.")
    else:
        print('Location: {} ({} - {} in {})'.format(response['country'], response['countryCode'], response['city'], response['regionName']))
        print('Timezone: {}'.format(response['timezone']))
        print('IP-Address: {}'.format(response['query']))
        print('As: {} - {}'.format(response['org'], response['as']))
