# https://thepacketgeek.com/scapy/sniffing-custom-actions/part-1/
# https://www.exploit-db.com/docs/48606
from scapy import packet
# from scapy.all import IP, UDP, DNS, DNSQR, sniff, send
from scapy.all import *
import socket
import sys

ipSrcList = []
ipDstList = []

def querySniff(packet):
    if IP in packet:
        ipSrc = packet[IP].src
        ipSrcList.append(packet[IP].src)
        ipDst = packet[IP].dst
        ipDstList.append(packet[IP].dst)
        # Make a response packet
        dr0 = IP(src=ipDstList[0],dst=ipSrcList[0]) /\
            UDP(sport=packet[UDP].sport, dport=53) /\
            DNS(id= packet[DNS].id, rd=1, qd=DNSQR(qname="foo.example.com"))

        send(dr0)

def main(interface="wlp2s0", hostnames="hostnames"):
    # https://www.binarytides.com/python-packet-sniffer-code-linux/
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    # List to hold the information we extract from the 
    # packets we grab
    packetList = []
    dnsQueryList = []
    
    print("Working...")
        # https://www.geeksforgeeks.org/packet-sniffing-using-scapy/
        # https://stackoverflow.com/questions/24792462/python-scapy-dns-sniffer-and-parser
        # https://null-byte.wonderhowto.com/how-to/build-dns-packet-sniffer-with-scapy-and-python-0163601/
    for i in range(5):
        # capture = sniff(iface = interface, filter = "port 53",
        #     prn = querySniff, store = 0, count = 1)
        capture = sniff(iface = interface, filter = "port 53", 
            count = 1, prn = querySniff)


        print("CAPTURE: ", capture)
        packetList += capture
    print("Done sniffing")

if __name__ == "__main__":
    # Take in command line arguments and pass onto main
    # main(sys.argv[1], sys.argv[2])

    # TODO remove before final implementation
    # Temporary main for testing purposes
    main("wlp2s0", "hostnames")

# Two processes: 1) capturing packets to  a data structure
# 2) Polling into data structure looking for a dns request,
# takes features out of dns, sends packets out to the network
# NEed to exract info out of the packets
