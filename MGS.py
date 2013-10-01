payload=''
for line in open('rfc5594.txt'):
    payload+=str(len(line) - len(line.rstrip()) - 1)
payload=payload.rstrip("0")
print 'Payload        : ' + payload
print 'Hexadecimal    : ' + ('%x' % int(payload,4))
payload_bin=bin(int(payload,4))[2:]
print 'Binary         : ' + payload_bin
print 'ASCII          : ' + ('%x' % int(payload_bin,2)).decode("hex")
payload_bin=bin(int(payload,4))[2:]+'0'
print 'Binary shift   : ' + payload_bin
print 'ASCII          : ' + ('%x' % int(payload_bin,2)).decode("hex")
print 'ASCII reverse  : ' + ('%x' % int(payload_bin,2)).decode("hex")[::-1]
