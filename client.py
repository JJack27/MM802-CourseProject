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

    ''' Step 3 : profiling
    when update profile, send a small data trunk fo server (e.g. "LOL")
    get queuing delay from server
    calculate queuing dalay will be done by server side,
    save the new queuing delay '''
    def Profiling(self,serverDic,folder_name, profile_type):
        if os.path.exists(folder_name):
            shutil.rmtree(folder_name)
        os.makedirs(folder_name)

        if profile_type == "greedy" :
            for sid in serverDic:
                fileName = folder_name + "/" + str(sid) + ".json"
                data = {
                  "sid" : sid,
                  "rrt" : serverDic[sid][0] + serverDic[sid][1]
                }
                with open(fileName, 'w') as json_file:
                    json.dump(data, json_file)


        elif profile_type == "mixed":
            # get another dict cid : [rrt1, rrt2....]
            v = defaultdict(list)
            for key, value in serverDic.items():
                value = list(value)
                v[value[2]].append(value[0] +value[1] )

            # save for each cluster, with average rrt
            for key, value in v.items():
                fileName = folder_name + "/" + str(key) + ".json"
                data = {
                    "cid" : key,
                    "rrt" : np.mean(np.array(v[key]))
                }
                with open(fileName, 'w') as json_file:
                    json.dump(data, json_file)


    ''' Step 4: greedy algorithm '''
    def greedy(folderProfiles,total_data,N):

        # direct to the folder
        profile_dic={}
        if not os.path.exists(folderProfiles):
            print("No profiles found!")
        if folderProfiles == "greedyProfiles":
            tag = 'sid'
        elif  folderProfiles == "mixedProfiles":
            tag = 'cid'


        # read json data from profile dictionary
        path_to_dir = os.getcwd()+"/" + folderProfiles
        for filename in os.listdir(path_to_dir):
            with open(os.path.join(path_to_dir, filename), 'r') as f:
                data=json.load(f)
                profile_dic[data[tag]] = data['rrt']


        # sort the profile and choose best 50 servers
        serverDic_sort={k: v for k, v in sorted(profile_dic.items(), key=lambda item: item[1])}
        serverDic_choose=dict(itertools.islice(serverDic_sort.items(), N))
        serverDic = serverDic_choose


        # initialization of dictionaries and portion rate
        temp_dic={}
        data_dic = np.zeros(N)
        data_dic[0] = total_data
        portion=2

        #implementation of greedy algorithm
        current_latency=np.inf
        for k in range (1,N):
            flag=True
            while flag:
                for i in range (0, k-1):
                    temp_dic[i]= data_dic[i]
                    data_dic[i]=data_dic[i]-portion

                data_sum=0
                for j in range (0,k-1):
                    data_sum+=data_dic[j]
                    data_dic[k]=total_data-data_sum

                max_latency=max(list(serverDic.values())[0:k])
                # print(list(serverDic.values())[0:k])
                # print(max_latency)

                if max_latency < current_latency:
                    flag=True
                    current_latency=max_latency
                else:
                    flag=False
                    for x in range (0,k-1):   # 1,2,3,4,...k
                        data_dic[x]=temp_dic[x]


        return data_dic, serverDic, current_latency




if __name__ == "__main__":
    pass
