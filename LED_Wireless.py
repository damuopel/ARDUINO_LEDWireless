import socket
import pyfirmata
import time
# ARDUINO
board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()
led_pin = board.get_pin('d:13:o')
# UDP
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = ('192.168.0.14', 8080)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)
    print('received {} bytes from {}'.format(len(data), address))
    print(data)
    # Send data to arduino
    if data.decode() == 'OUT':
        print('Closing connection...')
        # Close arduino
        board.exit()
        sock.close()
        break
    else:
        if data.decode() == 'ON':
            print('LED ON')
            led_pin.write(1)
        elif data.decode() == 'OFF':
            print('LED OFF')
            led_pin.write(0)
        time.sleep(0.1)

            
        
    
    