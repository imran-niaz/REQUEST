import requests
import json

# File containing the payloads
payloads_file = input("Enter the file containing the payloads: ")

# Read the payloads from the file
with open(payloads_file, 'r') as f:
    payloads = f.read().splitlines()

url = input("Enter the URL to send a request to: ")

#create a session
if response.headers['Content-Type'] == 'application/json':
    data = json.loads(response.text)
else:
    data = response.text

session = requests.Session()
if response.ok:
    data = json.loads(response.text)
else:
    data = response.text


#loop through the payloads
for payload in payloads:
    try:
        # send a GET request
        response = session.get(url, params={'payload': payload})
        # check for the status code
        if response.status_code not in [403, 404]:
            #parse the json response
            data = json.loads(response.text)
            #save the response in a file
            with open('response.txt', 'a') as f:
                json.dump(data, f)
                f.write('\n')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')


print("Responses saved to response.txt")

