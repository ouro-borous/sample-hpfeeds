import sys
import hpfeeds

PUBCHANNEL = "pub_client"

def main():
    

    command = ""
    while command != 'quit':
        print("Ready to publish on channel", PUBCHANNEL, ". Awaiting payload:")
        command = input()
        client = hpfeeds.new('localhost', 20000, PUBCHANNEL, 'password')
        client.publish("a.client.sample", command)
        
        client.close()

if __name__ == '__main__':
    try: sys.exit(main())
    except KeyboardInterrupt:sys.exit(0)