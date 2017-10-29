#Import Modules

import socket

#Address Space, by default I have this set to a /24
#This is currently only set up for a /24 or smaller.
addressSpace = 255

#This holds the results of the port scan.
results = []

#Enter ports you want scanned into the below array
ports = []

#Initializing the Address variable
address = ""

#Itterator for the while loop
i = 0

while(i < addressSpace):
	#Stores Working ports for this address
	workingPorts = []
	#Stores Failed Ports for this address
	failedPorts=[]

	#Add one to the last subnet
	i += 1;

	#This can be changed to what ever address space you want to use.
	#For this build it was 192.168.0.X
	address = "192.168.0." + str(i)


	print("Testing address: " + address)

	
	for port in ports:
		#Build Socket
		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		#Set Timeout to reduce the time for script to run
		#This can be changed for areas with large latency
		soc.settimeout(1)
		print("  testing port:", port)
		try:
			#Establish the socket
	   		soc.connect((address, port))

	   		#If it worked, log in the console, then add it to the working port array 
	   		print("     SUCCESS")
	   		workingPorts.append(port)
		except Exception as e: 
			#If failed, log to the console, then add it to the failed port array.
			print("     FAIL!")
			failedPorts.append(port)
			
		finally:
			#Close the socket
			soc.close()

	#Build a temp array to house the information related to this addresses scan		
	tempResults= [address,workingPorts,failedPorts]
	#Push temp results to the results array for later
	results.append(tempResults)
	
	
#Present results after all scans complete
print("Results....")
print("----------------------------------")
for result in results:
	print("Address: " + result[0])

	print("-----------------------")
	print("Open ports")
	print("-----------------------")

	for x in result[1]:
		print(x)

	print("-----------------------")
	print("Closed ports")
	print("-----------------------")

	for x in result[2]:
		print(x)

	print("   ")


	print("----------------------------------")
