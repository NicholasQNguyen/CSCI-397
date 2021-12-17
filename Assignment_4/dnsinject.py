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
    dr0 = IP(src=packet[IP].dst,dst=packet[IP].src) /\
        UDP(sport=packet[UDP].sport, dport=53) /\
        DNS(id= packet[DNS].id, rd=1, qd=DNSQR(qname="example.com"))

    send(dr0)

def main(interface="wlp2s0", hostnames="hostnames"):
    
    # https://www.w3schools.com/python/python_file_open.asp
    f = open(hostnames, "r")
    
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
    print("Done sniffing")

if __name__ == "__main__":
    # Take in command line arguments and pass onto main
    # main(sys.argv[1], sys.argv[2])

    # TODO remove before final implementation
    # Temporary main for testing purposes
    main("wlp2s0", "hostnames")
