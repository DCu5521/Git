import requests

# input is the URL of the Swagger JSON file
swagger_json_url = input("http://petstore.swagger.io/: ")

# send a GET request to the URL and store the response in a variable
response = requests.get(swagger_json_url)

# check if the request was successful
if response.status_code == 200:
    # parse the JSON data and store it in a variable
    swagger_data = response.json()
    # extract the endpoints
    endpoints = [route['path'] for route in swagger_data['paths'].values()]
    # output the endpoints
    print("Endpoints:", endpoints)
else:
    print("Failed to load the Swagger JSON file. Error code:", response.status_code)

