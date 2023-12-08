# aoc day 13
import json
import logging
logging.basicConfig(level=logging.DEBUG)

def get_packet_pairs(file_location):
    with open(file_location) as input:
        packets = input.read()
        return packets.split('\n\n')

def compare(packet1 , packet2):
    logging.debug(f'compare types {type(packet1)} and {type(packet2)}')
    logging.debug(f'compare values {packet1} and {packet2}')
    for i in range(len(packet1)):
        if i == len(packet2):
            return False
        if type(packet1[i]) == type(packet2[i]):
            if type(packet1[i]) == type(1):
                logging.debug(f'packet1 is an int {packet1[i]}')
                if packet1[i] > packet2[i]:
                    return False
            if type(packet1[i]) == type([]):
                logging.debug(f'packet1 is a list {packet1[i]}')
                if not compare(packet1[i],packet2[i]):
                    return False
                if len(packet2[i]) == 0:
                    return False
        else:
            if type(packet1[i]) == type(1):
                if not compare([packet1[i]],packet2[i]):
                    logging.debug(f'compare values {packet1} and {packet2}')
                    return False
            if type(packet1[i]) == type([]):
                if not compare(packet1[i],[packet2[i]]):
                    logging.debug(f'compare values {packet1} and {packet2}')
                    return False
    return True




#def compare(packet1 , packet2):
#    logging.debug(f'compare types {type(packet1)} and {type(packet2)}')
#    logging.debug(f'compare values {packet1} and {packet2}')
#    if type(packet1) == type(packet2):
#        if type(packet1) == type(1):
#            logging.debug(f'packet1 is an int {packet1}')
#            if packet1 > packet2:
#                return False
#            if packet1 < packet2:
#                return True
#        if type(packet1) == type([]):
#            logging.debug(f'packet1 is a list {packet1}')
#            if len(packet1) == 0:
#                return True
#            if len(packet2) == 0:
#                return False
#            if packet1[0] == packet2[0]:
#                return compare(packet1[1:], packet2[1:])
#            if type(packet1[0]) == type(packet2[0]):
#                logging.debug(f'packet subelements {packet1[0]} vs {packet2[0]}')
#                if type(packet1[0]) == type(1):
#                    if packet1[0] < packet2[0]:
#                        return True
#                    if packet1[0] == packet2[0]:
#                        return compare(packet1[1:], packet2[1:])
#                    if packet1[0] > packet2[0]:
#                        return False
#                else:
#                    logging.debug(f'compairing nested arrays')
#                    return compare(packet1[0], packet2[0])

def compare_packets(packets):
    [packet1, packet2] = packets.strip().split('\n')
    packet1 = json.loads(packet1)
    packet2 = json.loads(packet2)
    return compare(packet1, packet2)
    


packet_pairs = get_packet_pairs('final_input.txt')
correct_indexes = []
for packet_num in range(len(packet_pairs)):
    logging.debug(f'compairing packet pair {packet_num}')
    if compare_packets(packet_pairs[packet_num]):
        correct_indexes.append(packet_num+1)
    print(sum(correct_indexes))



