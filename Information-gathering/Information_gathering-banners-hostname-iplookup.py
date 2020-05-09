import sys
import requests
import socket
import json

# no arguements on command line than print this message
if len(sys.argv) < 2:
    print("usage:" + sys.argv[0] + "<url>")
    sys.exit(1)

req = requests.get("https://" + sys.argv[1])
print("\n" + str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])
print("\n The IP address of " + sys.argv[1] + "is" + gethostby_ + "\n")

# using api ipinfo.io for getting info about longitudes and langitudes
# we also provided that we want our response to be in json
req_two = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
# manipulating json with the json module
resp_ = json.loads(req_two.text)
# than we print location , city and region
print("location: " + resp_["loc"])
print("region: " + resp_["region"])
print("City: " + resp_["city"])
print("Country: " + resp_["country"])
