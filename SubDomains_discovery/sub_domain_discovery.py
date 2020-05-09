import requests
import sys

sub_list = open("sub-domains.txt").read()
subs = sub_list.splitlines()

for sub in subs:
    url_to_check = f'http://{sub}.{sys.argv[1]}'

    try:
        requests.get(url_to_check)

    except requests.ConnectionError:
        pass

    else:
        print("Valid Domain :", url_to_check)
