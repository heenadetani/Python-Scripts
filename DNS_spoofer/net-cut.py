import netfilterqueue


def process_packet(packet):
    print(packet)
    # Cut the internet connection as we are droping the packets here
    packet.drop()


queue = netfilterqueue.NetfilterQueue()
# 0 i.e queue_num to which we want to bind
# process_packet is the function that is to be executed by each packet present in the queue
queue.bind(0, process_packet)
queue.run()
