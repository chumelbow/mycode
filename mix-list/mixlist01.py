my_list = [ "192.168.0.5", "5060", "UP" ]
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + my_list[1] )
print("The last item in the list (state): " + my_list[2] )

# display only the IP addresses to the screen.
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# example 1 - add up the strings
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# example 2 - use the comma separator
print("IP addresses:", iplist[3], ", and", iplist[4])

# example 3 - use an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

