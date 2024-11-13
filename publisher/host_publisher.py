import sys
import hpfeeds


def main():
    

    command = ""
    while command != 'quit':
        command = input("Ready to publish. Awaiting command:")
        client = hpfeeds.new('localhost', 20000, 'popo_client', 'password')
        client.publish("a.client.sample", command)
        
        client.close()

if __name__ == '__main__':
    try: sys.exit(main())
    except KeyboardInterrupt:sys.exit(0)