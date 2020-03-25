from packet import Packet
import numpy as np


class Server:

    def __init__(self, server_id, congestion_rate, location):
        self.id = server_id
        self.congestion_rate = congestion_rate
        self.location = location
        self.buffer_count = 0   # the minimum serial number of packet received

    def receive_packet(self, packet):
        assert packet.server_id == self.id, "Incorrect destination for the packet"

        if packet.order > self.buffer_count or packet.correct == False:
            packet.response = False
        elif packet.order < self.buffer_count:
            packet.response = True
        else:
            self.buffer_count += 1
            packet.response = True
        packet.time_traveled += self.generate_delay()
        return packet

    def generate_delay(self):
        queue_delay = np.max([np.random.normal(self.congestion_rate / np.log(self.congestion_rate), np.sqrt(self.congestion_rate)), 0])
        return self.congestion_rate + queue_delay

if __name__ == "__main__":
    packets = []
    perturbed = []
    server = Server(0, 10, [20,100])
    for i in range(10):
        
        pkt = Packet("0-%d"%i, 0, 0, 0, 500)
        if np.random.random() < 0.3:
            perturbed.append(i)
            pkt.correct = False
        print(pkt)
        packets.append(pkt)
    print(perturbed)
    all_sent = False

    while not all_sent:
        all_sent = True
        print("------")
        for i in range(10):
            if packets[i].response != True:
                print("Sending",i)
                server.receive_packet(packets[i])
                if packets[i].response == False:
                    all_sent = False
                if np.random.random() > 0.3 and packets[i].correct == False:
                    packets[i].correct = True
    
        