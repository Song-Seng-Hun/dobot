import socket

dobot_socket = socket.socket()

ip = "192.168.235.6"

for i in range(29999, 30010):
    try:
        dobot_socket.connect((ip, i))
        print(ip + ":" + str(i) + "is working!!!!!")
        # break

    except:
        print(ip + ":" + str(i) + "is not working.")
        pass

print("done")

# ip = "192.168.235.6"

# for i in range(22000, 22001):
#     try:
#         dobot_socket.connect((ip, i))
#         print("Yeah")
#         break

#     except:
#         print(ip + ":" + str(i) + "is not working.")
#         pass

# print("done")

# ip = "192.168.235.3"

# for i in range(22000, 22001):
#     try:
#         dobot_socket.connect((ip, i))
#         print("Yeah")
#         break

#     except:
#         print(ip + ":" + str(i) + "is not working.")
#         pass

# print("done")