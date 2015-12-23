#!/usr/bin/env python
import sys, getopt, subprocess
from listener.Listener import Listener
import os
sys.path.insert(0, os.getcwd())

# Get the args
def main(argv):
    # Clear the screen
    subprocess.call('clear', shell=True)
    try:
        opts, args = getopt.getopt(argv, '', ['verbose=', 'protocol=' ])
        '''
         options:
          --verbose=true|false to tell or not user what tool is doing 
          --protocol=tcp|udp|icmp|all listen to {protocol} connections
        '''
   
        verbose = False
        protocol = ''
        
        for opt, arg in opts:
            
            if opt == '--verbose' and arg.lower() in ('true', 'y'):
                verbose = True
            
            if opt == '--protocol' and arg.lower() in ('tcp', 'udp', 'icmp', 'all'):
                protocol = arg.lower()

        listener = Listener(protocol, verbose)
        listener.getPartyStarted()
        
    except getopt.GetoptError:
        print('./ttw.py --verbose=true --protocol=tcp')
        sys.exit(2)
    except PermissionError:
        print('You must run it from root to get an access to all connections')
        sys.exit(2)
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
