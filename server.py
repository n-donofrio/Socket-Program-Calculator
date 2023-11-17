import socket

# Define the server host and port
server_host = 'localhost'
server_port = 12013  # You can choose any available port above 1024

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen(1)  # Listen for at most 1 connection

print(f"Server is listening on {server_host}:{server_port}")

# Function to perform math calculations
def calculate(expression):
    try:
        result = eval(expression)
        return str(result)
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except Exception:
        return "Input error. Re-type the math question again."

# Accept incoming client connections
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected by client on {client_address}")

    while True:
        data = client_socket.recv(1024).decode()
        result = calculate(data)

        print(f"Received question '{data}'; send back answer {result}")

        # Calculate the result and send it back to the client
        client_socket.send(result.encode())

        # Check for the end of input
        if data.strip() == '0/0':
            print("Received question '0 / 0 ='; end the server program")
            break

    # Close the client socket when done
    client_socket.close()
    if data.strip() == '0/0=':
        break

server_socket.close()
