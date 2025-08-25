import requests # Import requests library to handle HTTP requests

url = input("Enter your desired URL: ") # Define the URL via user input

try:
    response = requests.get(url, timeout=5) # Attempt to make a GET request with a timeout of 5 seconds
    
    print("Response code:", response.status_code) # Print HTTP status code
    
    if response.status_code == 200: # Check if the status code is 200
        print("Result: OK") # Print OK if TRUE
    else:
        print("Result: NOK") # Print NOK if FALSE
        
    response_time_ms = response.elapsed.total_seconds() * 1000 # Response time conversion from seconds to ms
    print("Response time:", int(response_time_ms), "ms") # Print response time in ms as INT. Without decimals it should be more than enough

except requests.exceptions.RequestException as e: # In case errors, timeouts or invalid URL occurs print the information about the exception
    print(f"Error details: {e}")