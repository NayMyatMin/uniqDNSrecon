#!python3 
#Written by NMM 

import json, requests, sys, csv, time, colorama
from colorama import Fore, Back, Style

# Compute DomainName from command line arguments.
if len(sys.argv) < 2:
    print('Usage: DNSrecon.py .<Domain_Name>\n')
    sys.exit()
domain = ' '.join(sys.argv[1:])



#The url for searching dns data set
url ='https://dns.bufferover.run/dns?q=%s' % (domain)
print(" ")
print(Fore.LIGHTBLUE_EX + "######################################")
print(Fore.LIGHTBLUE_EX + "# Developed by NMM, Enhanced by KMM  #")
print(Fore.LIGHTBLUE_EX + "######################################\r\n")
print(Fore.CYAN + "[*] Getting You Subdomains Please Wait..\r\n")

time.sleep(1)

response = requests.get(url)
response.raise_for_status()

#print(response.text)

DnsData = json.loads(response.text)
FDNS_Data = DnsData['FDNS_A']

SaveAsCsv = open('Results.csv','w')
resultWriter = csv.writer(SaveAsCsv, lineterminator='\n')

resultWriter.writerow(['Domain_Name','IP_Address'])

if FDNS_Data is None:
		print("No Results Found.. Please Tweak and Try Again.. \n")

else:
	for FDNS_Row in FDNS_Data:
		#Creating a Dictionary for the parsed Data
		FDNS_Dictionary = dict(x.split(",") for x in FDNS_Row.split(", "))
		#print(FDNS_Dictionary)

		for IP_addr, Name in FDNS_Dictionary.items():
			#print (f"The domain name \"{Name}\" has the IP address of \"{IP_addr}\"")
			print(Fore.GREEN + f"{Name}" + Fore.WHITE + " => " + Fore.RED + f" {IP_addr}\r")
			resultWriter.writerow((Name,IP_addr))

SaveAsCsv.close()

time.sleep(0.5)
print(Fore.RESET + " ")
print(Fore.LIGHTMAGENTA_EX + "Enjoy! our MF Collab @ github.com/naymyatmin & github.com/justasimplehacker \r\n")
print(Style.RESET_ALL)