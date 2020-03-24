from packet import Packet
from abc import ABC, abstractmethod


class BaseClient:

    '''
    Initialize a client
    Argument:
        - client_id: int, decided by the system
        - known_server: all servers that are availiable for clients to connect
    '''
    def __init__(self, client_id, location, known_servers):
        self.id = client_id
        self.links = {}                 # key: link_id | value: link object
        self.connected_servers = {}     # key: server id | value: link_id
        self.packet_record = {}         # key: packet id | value: RTT of ACK
        self.packet_size = {}           # key: server id | value: size of packet
        self.known_servers = known_servers
        self.location = location

        # TODO: Decide what is the value of profile
        self.profiles = {}              # key: server id | value: TBD
        
        

    
    '''
    Given a link, connect self client to the given link
    Argument:
        - link: A link object
    '''
    def add_link(self, link):
        assert (link.id not in self.links.keys()), "Given link is already connected"
        assert (link.server_id not in self.connected_servers.keys()), "Given server is already connected"
        self.links[link.id] = link


    '''
    Given a link id, delete the link according to the link id
    Argument:
        - link_id: int
    '''
    def delete_link(self, link_id):
        try:
            pop_link = self.links.pop(link_id)
            self.connected_servers.pop(pop_link.server_id)
        except:
            pass

    '''
    ! Need to override this method when implementing children class !
    generate packets based on profiling and redundancy algorithms
    '''
    @abstractmethod
    def init_packet(self):
        pass

    '''
    ! Need to override this method when implementing children class !
    get response from the server and update self.profile and self.packet_size
    '''
    @abstractmethod
    def get_response(self, packet):
        pass



if __name__ == "__main__":
    pass
