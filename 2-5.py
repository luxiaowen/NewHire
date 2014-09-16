#!/usr/bin/python
#ip+time=>identical
ipAddTime = {}
ipList=[]
f = open('ipHttpData','r')

for log_line in f.readlines():
    line_list = log_line.split(' ')
    uniIp = line_list[0]
    if uniIp not in ipList:
        ipList.append(uniIp)    
    ip = line_list[0],line_list[3][1:18]
    if ip in ipAddTime:
        ipAddTime[ip]+=1
    else:
        ipAddTime[ip]=1

print "Unique IP:"
for ip in ipList:
    print ip
print "# of unique IP:",len(ipList)

print "Issue IP:"
for ip in ipAddTime.keys():
    if ipAddTime[ip] > 30:
        print ip,"request",ipAddTime[ip],"times"

f.close()
