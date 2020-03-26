from utils import *
import numpy as np

class Link:

    def __init__(self, client, server):
        self.client_id = client
        self.server_id = server 
        self.distance = distance_2d(client.location, server.location)

    def generate_delay(self):
        queue_delay = np.max([np.random.normal(self.distance / np.log(self.distance), np.sqrt(self.distance)), 0])
        return self.distance + queue_delay

    # drop packet based on the distance between client and server
    # the further they are, the higher probability it is
    def drop_packet(self, packet):
        if np.random.random() < (sigmoid(self.distance) / 10):
            packet.correct = False


if __name__ == "__main__":
    pass