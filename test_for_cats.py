import requests
import os
import ssl
import socket
from datetime import datetime, timedelta
import pytz
import warnings
from urllib3.exceptions import InsecureRequestWarning
from email.utils import parsedate_to_datetime


# This function checks if a web page is served correctly
def check_web_page(url):
    try:
        # Suppress only the single warning from urllib3 needed.
        warnings.filterwarnings('ignore', category=InsecureRequestWarning)
        
        # Send a GET request to the URL
        # The verify=False parameter allows to make a request without SSL certificate verification
        # This is not recommended in production code, it's used here for demonstration purposes
        response = requests.get(url, verify=False)
        
        # If the response status code is not 200, raise an HTTPError
        response.raise_for_status()
        print(f"\033[92mWeb page served correctly with status code  -  {response.status_code}\033[0m")
        return response
    except requests.HTTPError as http_err:
        print(f"\033[92mHTTP error occurred: {http_err}\033[0m")
    except Exception as err:
        print(f"\033[92mAn error occurred: {err}\033[0m")

# This function prints the current date and time

def check_date_in_response(response):
    # Get the current date in Israel timezone
    currentDate = datetime.now(pytz.timezone('Israel')).date()
    #print(f"Current date in Israel timezone: {currentDate}")

    # Get the date from the response
    responseDateStr = response.headers['Date']  # assuming the date string is in the 'Date' header
    #print(f"Date string in response header: {responseDateStr}")
    
    # Parse the date from the response header and convert it to Israel timezone
    responseDate = datetime.strptime(responseDateStr, '%a, %d %b %Y %H:%M:%S %Z')
    responseDate = responseDate.replace(tzinfo=pytz.UTC).astimezone(pytz.timezone('Israel')).date()
    #print(f"Parsed date from response header: {responseDate}")

    # Check if the response date is the same as the current date
    if responseDate != currentDate:
        print("\033[91mThe date in the response is not correct.\033[0m")
    else:
        print("\033[92mThe date in the response is correct.\033[0m")

    print(f"\033[92mCurrent Date:   {currentDate}\033[0m")
    print(f"\033[92mResponse Date:  {responseDate}\033[0m")
    
def verify_ssl_cert(host, port, cert_file):
    # Create a new SSL context
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=cert_file)

    # Create a socket and connect to the server
    try:
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                print(ssock.getpeercert())
                print(f"\033[92mThe certificate is correct - OK\033[0m")
    except ssl.SSLError as e:
        print(f"\033[92mError: {e}\033[0m")

# This function asks the user for the host address, port number, and certificate path
# This function asks the user for the host address, port number, and certificate path
def get_user_input(host='localhost', port=80, cert_file=None):
    print("\033[96mPlease enter the following details:\033[0m")
    host = input(f"\033[96mHost address (default: {host}): \033[0m") or host
    port = int(input(f"\033[96mPort number (default: {port}): \033[0m") or port)
    cert_file = input(f"\033[96mCertificate path (default: {cert_file}): \033[0m") or cert_file
    return host, port, cert_file

# Get user input
host, port, cert_file = get_user_input()

# Construct the URL
url = f'https://{host}/'
# Check the web page
response = check_web_page(url)
# Print the current date and time
check_date_in_response(response)
# Verify the SSL certificate
verify_ssl_cert(host, port, cert_file)