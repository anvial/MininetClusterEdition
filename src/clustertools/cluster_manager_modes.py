from src.malwaretools.Malware_Propagation_Director import Malware_propagation_director
from src.CLI_Director                              import CLI_director
#from main                                          import logger_MalwareProp
from config.config_constants                       import MALWARE_PROP_STEP_NUMBER



def malware_propagation_mode(malware_node_list):
    '''Launching Malware propagation mode.

    Args:
        malware_node_list: Infection map of hosts in network graph.
    '''
    # prepare malware director
    malware_director = Malware_propagation_director()

    init_population_number = malware_director.get_infected_nodes_number()
    #logger_MalwareProp.info("Try\t\t\tSuccess\t\t\tCurrent\t\t\tTotal")
    #logger_MalwareProp.info("0\t\t\t" + "0\t\t\t" + str(init_population_number) +
    #                        '\t\t\t' + str(len(malware_node_list)))
    malware_director.set_init_population(init_population_number)
    malware_director.propagation_loop(MALWARE_PROP_STEP_NUMBER)
    malware_director.show_node_list()
    print("initial population number = " + str(init_population_number))
    print("total population number = ")

    malware_director.stop_malware_center()


def cli_mode(host_map, host_to_node_map, host_IP_map, ssh_chan_map, switch_num, h_and_sw_node_map):
    '''Launching CLI node.

    Args:
        host_map: Host IP address to host name map.
        host_to_node_map: Host to node IP address map.
        host_IP_map: Host name to host IP map.
        ssh_chan_map: SSH session to cluster node map.
        switch_num: Number of switches (not leaves node in graph) in network.
        h_anw_sw_node_map: Map, that define which nodes in graph switches, and which are hosts.
    '''
    cli_director = CLI_director(host_map, host_to_node_map, host_IP_map, ssh_chan_map, switch_num, h_and_sw_node_map)
    cli_director.cmdloop()