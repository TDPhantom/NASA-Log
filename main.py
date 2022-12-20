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
        FileType.append(line.split(" "))
except UnicodeDecodeError:
        print("uh-oh")



from collections import Counter
import matplotlib.pyplot as plt

c = Counter(ip_adresses)
k = Counter(Files)
t = Counter(Times)
# f = Counter(FileType)

Logs = Counter(ip_adresses)


print(Logs.keys)
print(Logs.values)

plt.bar(Logs.keys(), Logs.values(),) 

plt.show()


# print(c)
# print(k)
# print(t)
# print(f)
#
