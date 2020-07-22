# Treck20-Related
PoC for CVE-2020-11896 Treck TCP/IP stack and device asset investigation

## Protocol stack inspection

As many manufacturers adopt the Treck protocol stack, some manufacturers refer to the Treck protocol stack by way of hardware IP cores. It is not enough to identify vulnerabilities through device fingerprints alone. How to detect whether the target device is the Treck protocol stack becomes the key to asset investigation.

Here are the Treck protocol stack fingerprint detection method:

The Treck protocol stack customizes an ICMP packet of type 165 (0xa5), and once it receives a ICMP packet of type 165, it will reply with an ICMP packet response of type 166.
First, send an ICMP request packet to the target, where type=0xa5, code=0. Then, receive the icmp response packet data returned by the target, where type = 0xa6, code = 0, and the six bytes after the 9th byte of the ICMP message are 0x01,0x51,0x35,0x28,0x57,0x32 (big endian) or 0x51,0x01,0x28,0x35,0x32,0x57 (little endian).Satisfying the above-mentioned conditions indicates that the target device is the treck protocol stack.
