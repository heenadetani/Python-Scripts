import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac",
                      help="new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error(
            "[-] please specify an interface,and use --help for more info")
    elif not options.new_mac:
        parser.error(
            "[-] please specify a new MAC,and use --help for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call("ifconfig " + interface + " down ", shell=True)
    subprocess.call("ifconfig " + interface +
                    " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up ", shell=True)


options = get_arguments()
change_mac(options.interface, options.new_mac)
