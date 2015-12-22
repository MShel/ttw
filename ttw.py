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
        opts = getopt.getopt(argv, '', ['verbose=', 'protocol=' ])
        '''
         options:
          --cid=CID of connection
          --verbose=true|false to tell or not user what I'm doing
          --protocol=tcp listen to all tcp connections and only them
          --destination=google.com listen only to connections to the host
          --log=/tmp/log.txt dump all the traffic to
          --port=21 listen to all the stuff been send to port
        '''
   
        verbose = False
        protocol = ''
        
        for opt, arg in opts:
            
            if opt == '--verbose':
                if arg.lower() in ('true', 'y'):
                    verbose = True
            
            if opt == '--protocol' :
                if arg.lower() in ('tcp', 'udp', 'icmp', 'all'):
                    protocol = arg.lower()

        listener = Listener(protocol, verbose)
        listener.getPartyStarted()
        
    except getopt.GetoptError:
        print('ttw.py verbose=true')
        sys.exit(2)
    except 'otherError':
        sys.exit(255)
    except 'KeyboardInterrupt':
        print('Keyboard interrupted')
        sys.exit(2)
        
if __name__ == "__main__":
    main(sys.argv[1:])
