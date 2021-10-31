15,7 +15,7 @@
for i in range(0, len(results)):
    # psrc stands for Source IP
    # hwsrc stands for Destination MAC Address
    temp = {"ip":results[i][0].psrc,"mac":results[i][1].hwsrc}
    temp = {"ip":results[i][1].psrc,"mac":results[i][1].hwsrc}
    output.append(temp)
for i in range(len(output)):
    print(output[i])
