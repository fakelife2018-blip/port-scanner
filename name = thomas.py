IP1 = input("Please enter your first IP: ")
IP2 = input("Please enter your second IP: ")
IP3 = input("Please enter your third IP: ")

x = [IP1, IP2, IP3]

for i, ip in enumerate(x, 1):
    print(i, "-", ip)