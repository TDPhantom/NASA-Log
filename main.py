#Do-Now 12/14

file = open("NASA_access_log_Jul95")
ip_adresses = []


try:
    for line in file:
        ip_adresses.append(line.split(" ")[0])
except:
        print("uh-oh")

print(ip_adresses)

#