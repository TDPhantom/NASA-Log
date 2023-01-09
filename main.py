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
# t = Counter(Times)
# f = Counter(FileType)

Logs = Counter(ip_adresses)
Filess = Counter(Files)

newDicts = dict()
for (key, value) in Filess.items():
    if value > 2500 :
        newDicts[key] = value

newDict = dict()
for (key, value) in Logs.items():
    if value > 500 :
        newDict[key] = value


print(newDict)
print(newDicts)


print(Logs.keys)
print(Logs.values)

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

C = ["Green", "Red" , "Blue" , "Yellow" , 'black' ]
CC = ["crimson", "cyan" , "navy" , "yellow" , "lightpink" ,"coral"]

plt.bar(newDict.keys(), sorted(newDict.values()),color = C ) 

plt.xticks(rotation=30, ha='right')
plt.title("Common Ip Addresses", fontdict = font1)
plt.xlabel("Ip Addresses", fontdict = font1)
plt.ylabel("Number of Ip Adresses", fontdict = font2)
plt.subplots_adjust(bottom=0.312)

plt.show()

plt.bar(newDicts.keys(), sorted(newDicts.values()), color = CC) 
plt.xticks(rotation=50, ha='right')
plt.title("Files from NASA", fontdict = font1)
plt.xlabel("Most Common Files", fontdict = font1)
plt.ylabel( "Files", fontdict = font2)
plt.subplots_adjust(bottom=0.613)

plt.show()


# print(c)
# print(k)
# print(t)
# print(f)
#
