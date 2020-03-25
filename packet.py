from utils import *

class Packet:
    def __init__(self, client_id, server_id, link_id, size ):
        self.client_id = client_id
        self.server_id = server_id
        self.link_id = link_id

        assert size > 0, "Incorrect size"
        self.size = size

        # variable to decide if this packet is perturbed during transfer 
        self.correct = True

        self.time_traveled = 0


    def add_travel_time(self, travel_time):
        assert travel_time > 0, "Invalid travel time"
        self.time_traveled += travel_time



if __name__ == "__main__":
    pk1 = Packet(0,0,0,50)
    pk2 = Packet(0,0,0,50)

    # Test size
    try:
        pk3 = Packet(0,0,0, -1)
    except:
        pass
    else:
        raise Exception("Size not pass")

    print("Pass!")

