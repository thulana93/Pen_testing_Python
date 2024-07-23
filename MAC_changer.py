import subprocess
import optparse
import re

parser = optparse.OptionParser()
parser.add_option("--interface", dest="interface", help= "Interface to change MAC")
parser.add_option("--mac", dest="MAC", help="New MAC address")
(options, arguments) = parser.parse_args()
interface= options.interface
MAC=options.MAC

def main(interface, MAC):
    subprocess.call('sudo ifconfig ' + interface + ' down', shell=True)
    subprocess.call('sudo ifconfig ' + interface +  ' hw ether ' + MAC, shell=True)
    subprocess.call('sudo ifconfig ' + interface + ' up', shell=True)
    results = subprocess.check_output(['ifconfig', interface])
    #print(results)
    results= results.decode('utf-8')
    mac_out=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:", results)
    if mac_out:
        if MAC == mac_out:
            print('[+] MAC Address is changed successfully')
        else:
            print('[-] MAC Address is not changed')
    else:
        print('[-] MAC Address not identified')
    
if __name__=="__main__":
    main(interface, MAC)