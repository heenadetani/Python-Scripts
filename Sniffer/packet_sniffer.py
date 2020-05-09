import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False,
                prn=process_sniffed_packet, filter="udp")


def process_sniffed_packet(packet):
    # print(packet)
    if packet.haslayer(http.HTTPRequest):
        print(packet)


sniff("eth0")
