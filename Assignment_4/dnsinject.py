# https://thepacketgeek.com/scapy/sniffing-custom-actions/part-1/
# https://www.exploit-db.com/docs/48606
from scapy import packet
from scapy.all import IP, UDP, DNS, DNSQR, sniff, send
import socket
import sys
import pyshark


ipSrcList = []
ipDstList = []

def querySniff(packet):
    if IP in packet:
        ipSrc = packet[IP].src
        ipSrcList.append(packet[IP].src)
        ipDst = packet[IP].dst
        ipDstList.append(packet[IP].src)

def main(interface="wlp2s0", hostnames="hostnames"):
    # https://www.binarytides.com/python-packet-sniffer-code-linux/
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    # List to hold the information we extract from the 
    # packets we grab
    packetList = []
    
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

    # capture.summary()
    # # https://stackoverflow.com/questions/19311673/fetch-source-address-and-port-number-of-packet-scapy-script
    # if packetList:
    #     for pkt in packetList:
    #         if DNS in pkt:
    #             ipSrc = pkt[DNS]
    #             ipDst = pkt[DNS]
    #             print("IP SOURCE: ", ipSrc)
    #             print("IP DESTINATION: ", ipDst)
    # https://0xbharath.github.io/art-of-packet-crafting-with-scapy/scapy/creating_packets/index.html
    dnsQuery = IP(dst="10.6.6.6") / UDP(dport=53) /DNS(rd=1, qd=DNSQR(qname="foo.example.com"))

    # print("PACKET LIST: ", packetList)
    # I'm able to send the packet which is cool
    send(dnsQuery)


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
