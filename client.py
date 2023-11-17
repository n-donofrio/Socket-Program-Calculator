import socket

# Define the server host and port
server_host = 'localhost'
server_port = 12013  # Use the same port as the server

# Create a socket to connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

print(f"Connected with server on {server_host}:{server_port}")

while True:
    expression = input("Enter a math question (e.g., x op y =): ")
    client_socket.send(expression.encode())

    # Check for the end of input
    if expression.strip() == '0/0':
        print("User input ends; end the client program")
        break

    result = client_socket.recv(1024).decode()
    print(f"Answer from server: {result}")

# Close the client socket when done
client_socket.close()
