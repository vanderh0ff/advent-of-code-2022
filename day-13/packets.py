# aoc day 13
import json
import logging
log = logging.getLogger()
log.setLevel(logging.DEBUG)

def get_packet_pairs(file_location):
    with open(file_location) as input:
        packets = input.read()
        return packets.split('\n\n')

def compare(packet1 , packet2):
    if type(packet1) == type(packet2):
        if type(packet1) == type(1):
            if packet1 > packet2:
                return False
            if packet1 < packet2:
                return True
        if type(packet1) == type([]):
            if len(packet1) == 0:
                return True
            if len(packet2) == 0:
                return False
            if packet1[0] == packet2[0]:
                return compare(packet1[1:], packet2[1:])
            if type(packet1[0]) == type(packet2[0]):
                if type(packet1[0]) == type(1):
                    if packet1[0] < packet2[0]:
                        return True
                    if packet1[0] == packet2[0]:
                        return compare(packet1[1:], packet2[1:])
                    if packet1[0] > packet2[0]:
                        return False
    else:
        log.debug(f'compare type mismatch {type(packet1)} and {type(packet2)}')
        if type(packet1) == type(1):
            compare([packet1], packet2)
        else:
            compare(packet1, [packet2])


def compare_packets(packets):
    [packet1, packet2] = packets.strip().split('\n')
    packet1 = json.loads(packet1)
    packet2 = json.loads(packet2)
    return compare(packet1, packet2)
    


packet_pairs = get_packet_pairs('input.txt')
for packets in packet_pairs:
    res = compare_packets(packets)
    print(res)



