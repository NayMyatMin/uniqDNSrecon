#!python3 
#Written by NMM

import json, requests, sys

# Compute DomainName from command line arguments.
if len(sys.argv) < 2:
    print('Usage: DNSrecon.py <Domain_Name>\n')
    sys.exit()
domain = ' '.join(sys.argv[1:])

#The url for searching dns data set
url ='https://dns.bufferover.run/dns?q=%s' % (domain)

response = requests.get(url)
response.raise_for_status()

#print(response.text)

DnsData = json.loads(response.text)
FDNS_Data = DnsData['FDNS_A']

if FDNS_Data is None:
		print("No Results Found.. Please Tweak and Try Again.. '\n")

else:
	for FDNS_Row in FDNS_Data:
		#Creating a Dictionary for the parsed Data
		FDNS_Dictionary = dict(x.split(",") for x in FDNS_Row.split(", "))
		#print(FDNS_Dictionary)

		for IP_addr, Name in FDNS_Dictionary.items():
			#print (f"The domain name \"{Name}\" has the IP address of \"{IP_addr}\"")
			print(f"{Name} => {IP_addr}")
	print('\n')