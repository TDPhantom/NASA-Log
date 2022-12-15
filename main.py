#Do-Now 12/14

file = open("NASA_access_log_Jul95")
ip_adresses = []
Files = []
Times = []
FileType = []

try:
    for line in file:
        ip_adresses.append(line.split(" ")[0])
        Files.append(line.split(" ")[6])
        Times.append(line.split(" ")[3].split(":")[0])
        FileType.append(line.split(" ")[6].split("/")[2])
except:
        print("uh-oh")



from collections import Counter
c = Counter(ip_adresses).most_common(1)
k = Counter(Files).most_common(1)
t = Counter(Times).most_common(1)
f = Counter(FileType).most_common(1)
print(c)
print(k)
print(t)
print(f)
#
