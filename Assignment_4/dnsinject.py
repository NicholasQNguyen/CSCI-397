# https://thepacketgeek.com/scapy/sniffing-custom-actions/part-1/
# https://www.exploit-db.com/docs/48606
from scapy.all import *
import sys

packetList = []


def querySniff(packet):
    packetList.append(packet)
    # Just hardcode in the values from hostnames for testing
    # If it's one of the packets we're trying to intercept, send
    # our interception packet
    # String slice to get just the dst ip
    if packet.summary()[30:38] == "10.6.6.6":
        dr0 = IP(src=packet[IP].dst, dst=packet[IP].src) /\
            UDP(sport=packet[UDP].sport, dport=53) /\
            DNS(id=packet[DNS].id, rd=1, qd=DNSQR(qname="foo.example.com"))
        send(dr0)
    elif packet.summary()[30:38] == "10.6.6.7":
        dr0 = IP(src=packet[IP].dst, dst=packet[IP].src) /\
            UDP(sport=packet[UDP].sport, dport=53) /\
            DNS(id=packet[DNS].id, rd=1, qd=DNSQR(qname="bar.example.com"))
        send(dr0)


def main(interface="wlp2s0", hostnames="hostnames"):

    print("Working...")
    # https://www.geeksforgeeks.org/packet-sniffing-using-scapy/
    # https://stackoverflow.com/questions/24792462/python-scapy-dns-sniffer-and-parser
    # https://null-byte.wonderhowto.com/how-to/build-dns-packet-sniffer-with-scapy-and-python-0163601/
    for i in range(5):
        capture = sniff(iface=interface, filter="port 53",
                        count=1, prn=querySniff)

        print("CAPTURE: ", capture)
    print("Done sniffing")

    dr0 = IP(src=packetList[0][IP].dst, dst=packetList[0][IP].src) /\
        UDP(sport=packetList[0][UDP].sport, dport=53) /\
        DNS(id=packetList[0][DNS].id, rd=1, qd=DNSQR(qname="example.com"))
    send(dr0)


if __name__ == "__main__":
    # Take in command line arguments and pass onto main
    main(sys.argv[1], sys.argv[2])
