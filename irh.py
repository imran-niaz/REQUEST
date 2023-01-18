import requests
from requests.exceptions import RequestException

def send_request(url, method='GET', data=None, headers=None):
    try:
        if method == 'GET':
            response = requests.get(url, timeout=5)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, timeout=5)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers, timeout=5)
        elif method == 'DELETE':
            response = requests.delete(url, timeout=5)
        else:
            raise ValueError(f"Invalid method: {method}")
        # Raise an exception for non-200 status codes
        response.raise_for_status()
        return response
    except RequestException as e:
        print(f'Error: {e}')
    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Something Else:",err)

# Get the URL and method from the user
url = input("Enter the URL to send a request to: ")

print("Select an option:")
print("1. GET")
print("2. POST")
print("3. PUT")
print("4. DELETE")

method_input = input()

if method_input == "1":
    method = "GET"
elif method_input == "2":
    method = "POST"
    data = input("Enter the request data (if any): ")
    headers = input("Enter the request headers (if any): ")
elif method_input == "3":
    method = "PUT"
    data = input("Enter the request data (if any): ")
    headers = input("Enter the request headers (if any): ")
elif method_input == "4":
    method = "DELETE"
else:
    print("Invalid option selected.")

# Send the request and store the response
response = send_request(url, method=method, data=data, headers=headers)

# Save the response
