import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    # wraping the payload of this packet with scapy IP layer
    scapy_packet = scapy.IP(packet.get_payload())
    print(scapy_packet.show())
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
# 0 i.e queue_num to which we want to bind
# process_packet is the function that is to be executed by each packet present in the queue
queue.bind(0, process_packet)
queue.run()
