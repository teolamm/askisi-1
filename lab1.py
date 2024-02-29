import requests
from datetime import datetime

url = input("please give a valid url: ")
if not url.startswith("http://"):
    url = "http://" + url

with requests.get(url) as response:

    print("\nthe headers of this website are:\n")
    for header in response.headers:
        print(header)

    server = response.headers.get("Server")
    cookies = response.cookies
    cookies_dict = response.cookies.get_dict()

    if server:
        print("\nthe server is:", server)
    else:
        print("\nno server found...")

    if cookies:
        print("\nthe cookies are:\n")
        #print(cookies)
        i = 0
        for cookie in cookies:
            print(list(cookies_dict)[i] + ", which expires at:", datetime.fromtimestamp(cookie.expires))
            i += 1
    else:
        print("\nno cookies found...\n")