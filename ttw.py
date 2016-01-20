#!/usr/bin/env python
import sys, getopt, subprocess
from listener.Listener import Listener
import os
from pprint import pprint

sys.path.insert(0, os.getcwd())

# Get the args
def main(argv):
    # Clear the screen
    subprocess.call('clear', shell=True)
    try:
        opts, args = getopt.getopt(argv, 'h', ['verbose=', 'protocol=', 'nic=', 'help=' ])
        '''
         options:
          --verbose=true|false to tell or not user what tool is doing 
          --protocol=tcp|udp|icmp|all listen to {protocol} connections
          --nic= wlan0|lo|eth0 network interfaces
        '''
   
        verbose = False
        protocol = 'all'
        nic = 'all'
        credentials = {}
        #here you can specify config for stat adapter for now its sqlite adapter
        adapterType = 'sqlite'
        credentials['dbFilePath'] = 'ttw'
        
        for opt, arg in opts:
            if opt in ('--help', '-h'):
                print('EX. python3 ttw.py --verbose=true --protocol=tcp --nic=wlan0')
                sys.exit(0)
            
            if opt == '--verbose' and arg.lower() in ('true', 'y'):
                verbose = True
            
            if opt == '--protocol' and arg.lower() in ('tcp', 'udp', 'icmp', 'all'):
                protocol = arg.lower()

            if opt == '--nic' and arg.lower() in Listener.getInterfaces():
                nic = arg.lower()
                
        listener = Listener(protocol, verbose, nic, adapterType, credentials)
            
        listener.getPartyStarted()
        
    except getopt.GetoptError:
        print('./ttw.py --verbose=true --protocol=tcp')
        sys.exit(2)
    except PermissionError:
        print('You must run it from root to get an access to all connections')
        sys.exit(2)
    #except Exception as e:
        #print(e)
        #sys.exit(2)
    except IndexError:
        print('Provided protocol is not supported')
        sys.exit(2)
    except KeyboardInterrupt:
        listener.printStatistic()
        sys.exit(1)
    except ImportError:
        print('You probably need to install netifaces: \n `pip install netifaces`')
        sys.exit(2)    
        
if __name__ == "__main__":
    main(sys.argv[1:])
