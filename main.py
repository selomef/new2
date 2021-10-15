import socket
from socket import AF_INET, SOCK_STREAM



msg = "\r\n My message"
endmsg = "\r\n.\r\n"
mailserver = ("mail.nyu.edu", 2525)
port = 2525
   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

   # Create socket called clientSocket and establish a TCP connection with mailserver and port

   # Fill in start

clientSocket = socket.socket(AF_INET, SOCK_STREAM)

clientSocket.connect(mailserver, port)

   # Fill in end

recv = clientSocket.recv(1025)
#print(recv)
#if recv[:3] != '220':
       #print('220 reply not received from server.')
      #print("220 reply not received from server")
   # Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1025).decode()
print(recv1)
#if recv1[:3] != '250':
       #print('250 reply not received from server.')
       #print('250 reply not received from server')
   # Send MAIL FROM command and print server response.
   # Fill in start
mailFrom = "MAIL FROM: <sf3809@nyu.edu> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1025)
print(recv2)
#if recv1[:3] != '250':
    #print('250 reply not received from server.')

# Fill in end

   # Send RCPT TO command and print server response.
   # Fill in start
rcptTo = "RCPT TO: <selomef@gmail.com> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1025)
print(recv3)
#if recv1[:3] != '250':
    #print('250 reply not received from server.')

# Fill in end

   # Send DATA command and print server response.
   # Fill in start
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1025)
#print(recv4)
#if recv1[:3] != '250':
    #print('250 reply not received from server.')
   # Fill in end

   # Send message data.
   # Fill in start

recv_msg = clientSocket.recv(1025)
#print(recv_msg.decode())
#if recv1[:3] != '250':
    #print('250 reply not received from server.')

# Fill in end

   # Message ends with a single period.
   # Fill in start
#print(recv_msg.decode() + '.')
   # Fill in end

   # Send QUIT command and get server response.
   # Fill in start
clientSocket.send("QUIT\r\n".encode())
message = clientSocket.recv(1025)
#print(message)
clientSocket.close()
   # Fill in end

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
