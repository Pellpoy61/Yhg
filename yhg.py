import socket
import time
while true
print("""
 __     ___    _  _____ 
 \ \   / / |  | |/ ____|
  \ \_/ /| |__| | |  __ 
   \   / |  __  | | |_ |
    | |  | |  | | |__| |
    |_|  |_|  |_|\_____|
""")

startti = input("Welcome\n\n")

if startti == "scanner":
    print("Loading")
    time.sleep(3)
    kysy = input("Start scanning? (yes/no)\n")

    if kysy.lower() == "yes":
        def get_ip_address(url):
            try:
                ip_address = socket.gethostbyname(url)
                print(f"The IP address of {url} is: {ip_address}")
            except socket.error as e:
                print(f"Error: {e}")

        # Take user input for the URL
        user_url = input("Enter the URL: ")

        # Ask for confirmation before scanning
        confirmation = input(f"Do you want to find the IP address of {user_url}? (y/n): ")

        if confirmation.lower() == 'y':
            # Find the IP address of the specified URL
            get_ip_address(user_url)
        else:
            print("IP address scanning canceled.")

elif startti.lower() == "attack":
    print("Loading")
    time.sleep(3)
    kysyy = input("Open attack program yes/no\n\n")

    if kysyy.lower() == "yes":
        def send_packets(ip, port, message):
            try:
                udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                while True:
                    user_input = input("Type 'stop' to end or enter a message to send: ")
                    if user_input.lower() == 'stop':
                        break
                    udp_socket.sendto(message.encode(), (ip, port))
                    print("Packet sent successfully.")
            except socket.error as e:
                print(f"Error: {e}")
            finally:
                udp_socket.close()

        # Take user input for the target IP address and port
        target_ip = input("Enter the target IP address: ")
        target_port = int(input("Enter the target port: "))

        # Message to send
        message_to_send = input("Enter the initial message to send: ")

        # Call the function to send packets until 'stop' is entered
        send_packets(target_ip, target_port, message_to_send)
break
