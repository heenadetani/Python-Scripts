from scapy.all import *
import os

iface = "wlan0"


def h_packet(packet):
    # checking for probe requests response and association requests
    if packet.haslayer(Dot11ProbeReq) or packet.haslayer(Dot11ProbeResp) or packet.haslayer(Dot11AssoReq)
    print("SSID identified" + packet.info)


# enabling monitor mode into the wireless card
os.system("iwconfig" + iface + "mode monitor")

print("Sniffing traffic on interface " + iface)
sniff(iface=iface, prn=h_packet)
