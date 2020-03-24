from utils import *


class BaseClient:
    def __init__(self, client_id, known_servers):
        self.id = client_id
        self.links = {}     # key: link_id; value: link object
        self.profiles = []
        self.known_servers = known_servers
        self.packet_size = {}
    
    '''
    Given a link, connect self client to the given link
    Argument:
        - link: A link object
    '''
    def add_link(link):
        assert (link.id not in self.links.keys()), "Given link is already connected"
        self.links[link.id] = link


    '''
    Given a link id, delete the link according to the link id
    Argument:
        - link_id: int
    '''
    def delete_link(link_id):
        try:
            self.links.pop(link_id)
        except:
            pass
    
        