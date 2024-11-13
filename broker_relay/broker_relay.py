import sys
import logging
logging.basicConfig(level=logging.WARNING)

import traceback
import json
import hpfeeds

# Information about other broker that I want to connect to
HOST = '127.0.0.1'
PORT = 20000
CHANNELS = ["a.client.sample"]
IDENT = 'tab_a'
SECRET = 'password'

RELAYCHAN = "a.channel"


def main():
    hpc = hpfeeds.new(HOST, PORT, IDENT, SECRET)
    print('connected to', hpc.brokername, file=sys.stderr)

    def on_message(ident, channel, payload):
        
        print(ident, "sent a notif on", channel, ". Relaying!", file=sys.stderr)
        hpc.publish(RELAYCHAN, payload)
        
        # try:
        #     dec = json.loads(str(payload))
        #     del dec['daddr']
        #     dec['identifier'] = ident
        #     enc = json.dumps(dec)
        # except:
        #     traceback.print_exc()
        #     print >>sys.stderr, 'forward error for message from {0}.'.format(ident)
        #     return
        
        #hpc.publish(RELAYCHAN, enc)

    def on_error(payload):
        print(' -> errormessage from server: {0}'.format(payload), file=sys.stderr)
        hpc.stop()

    hpc.subscribe(CHANNELS)
    print("Subbed!", file=sys.stderr)
    hpc.run(on_message, on_error)
    print("Cleaning!", file=sys.stderr)
    hpc.close()
    return 0


if __name__ == '__main__':
    try: sys.exit(main())
    except KeyboardInterrupt:sys.exit(0)
