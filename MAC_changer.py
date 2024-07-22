import subprocess

def main(interface, MAC):
    subprocess.call('sudo ifconfig ' + interface + ' down', shell=True)
    subprocess.call('sudo ifconfig ' + interface +  ' hw ether ' + MAC, shell=True)
    subprocess.call('sudo ifconfig ' + interface + ' up', shell=True)
    subprocess.call('ifconfig', shell=True)

if __name__=="__main__":
    main(interface='eth0', MAC='50:33:66:88:99:11')