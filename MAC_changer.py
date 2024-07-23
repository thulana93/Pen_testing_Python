import subprocess
import optparse

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
    subprocess.call('ifconfig', shell=True)

if __name__=="__main__":
    main(interface, MAC)