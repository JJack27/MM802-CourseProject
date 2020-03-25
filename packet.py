from utils import *

class Packet:

    # packet_id in the following format: serverId-packetOrder
    def __init__(self, packet_id, client_id, server_id, link_id, size):
        self.id = packet_id
        self.client_id = client_id
        self.server_id = server_id
        self.link_id = link_id
        self.order = int(packet_id.split("-")[1])
        assert size > 0, "Incorrect size"
        self.size = size

        # variable to decide if this packet is perturbed during transfer 
        self.correct = True

        self.time_traveled = 0
        self.response = None


    def add_travel_time(self, travel_time):
        assert travel_time > 0, "Invalid travel time"
        self.time_traveled += travel_time
    
    def __str__(self):
        string = "=======================\n"
        string += "Packet: %s\nFrom: %d\nTo: %d\nCorrect: %s\nSize: %f\nTime Traveled: %f\nResponse: %s\n" \
            %(self.id, self.client_id, self.server_id, str(self.correct), self.size, self.time_traveled, self.response)
        string += "======================="
        return string



if __name__ == "__main__":
    pk1 = Packet("0-0",0,0,0,50)
    pk2 = Packet("0-1",0,0,0,50)

    # Test size
    try:
        pk3 = Packet("0-1",0,0,0, -1)
    except:
        pass
    else:
        raise Exception("Size not pass")

    print("Pass!")

