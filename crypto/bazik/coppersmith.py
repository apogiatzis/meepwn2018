import time
import sys

def long_to_bytes(data):
    data = str(hex(long(data)))[2:-1]
    return "".join([chr(int(data[i:i + 2], 16)) for i in range(0, len(data), 2)])
    
def bytes_to_long(data):
    return int(data.encode('hex'), 16)

def main():
    e,N = (3L, 104444627595322899402492638169835048294986970619821522382724853607375677938894942474095823756446038305614312829183426681595269901662602664371215039573476690536104888585871142429077647296147110254138500256424360497072878570921904389823187789854830890727664911120741988236649088913165631005322586000495257977799L)
    c = 0x20375ebbb61e4841c9cb223fbbdd3bfc271fdfc581680ea1e8e6232b7a37a8d34e9979c0e0f44dac09efa840d8c3d74e59ec6477a2378221e7130d3b82602be37472df51621cc3e4b4be845c8c320051c9a712eafb50fe738c07bf01901d889981b3b0cea2abd3ef9771ae06de089791e83700627e2f8e5f83f17c082542a3da
    m = bytes_to_long("Your OTP for transaction #731337 in ABCXYZ Bank is 000000000.")
    P.<x> = PolynomialRing(Zmod(N), implementation='NTL')
    pol = (m + x)^e - c
    roots = pol.small_roots(epsilon=1/30)
    print("Potential solutions:")
    for root in roots:
       print(root, long_to_bytes(m+root))
	
main()

