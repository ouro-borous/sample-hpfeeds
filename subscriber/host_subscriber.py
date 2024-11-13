import sys
import hpfeeds


def on_message(identifier, channel, payload):
    print(identifier, payload)


def on_error(payload):
    print(' -> errormessage from server: {0}'.format(payload), file=sys.stderr)
    hpc.stop()


def main():
    hpc = hpfeeds.new('localhost', 20000, 'tab_b', 'password')
    print('connected to', hpc.brokername, file=sys.stderr)

    hpc.subscribe('a.channel')
    hpc.run(on_message, on_error)
    hpc.close()

if __name__ == '__main__':
    try: sys.exit(main())
    except KeyboardInterrupt:sys.exit(0)