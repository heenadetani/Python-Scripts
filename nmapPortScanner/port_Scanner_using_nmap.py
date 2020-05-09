import nmap
import sys

# taking command line arguements
target = str(sys.argv[1])
# ports for which we want to scan
ports = [21, 22, 80, 139, 443, 8080]
# initiating the nmap portScanner
scan_v = nmap.PortScanner()

print "\nScanning", target, "for ports 21,22,80,139,443 and 8080..\n"

for port in ports:
    # scanning the specified ports for target it gives the result in the form of dictionary
    portscan = scan_v.scan(target, str(port))
    print "Port", port, "is", portscan['scan'][target]['tcp'][port]['state']

# state of host
print "\nHost", target, "is", portscan['scan'][target]['status']['state']
