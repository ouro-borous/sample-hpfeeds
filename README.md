## Setup

The following are step by step instructions on how to get the hpfeeds components up and running on Debian. Make sure all these are running simultaneously!

### Getting source

```bash
sudo apt update ; sudo apt full-upgrade -y
git clone https://github.com/ouro-borous/sample-hpfeeds/
cd ./sample-hpfeeds
```

### Dependencies

Set up venv and install dependencies with:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install hpfeeds[broker]
```

### Broker

The broker should be the first service ran. The hpfeeds sample code works just fine for this. Make sure that the ```--auth``` flag is set to the file path of users.json - i.e. the broker should be called from the repo's root directory.

```bash
./broker.sh
```

### Relay

Next, we'll attach our relay program to the running broker. This code is set up for fully local testing, so there's no need to change IP addresses.

```bash
python ./broker_relay/broker_relay.py
```

### Subscriber

Next, we'll attach a subscriber to the secondary channel.

```bash 
python ./subscriber/host_subscriber.py
```

### Publisher

Finally, we'll connect to our original broker with a publisher and start publishing messages. Send any message you want and check to see if all components show activity. The subscriber at the end should display the same message if all works correctly. Send "quit" or input CTRL-C to stop the publisher.

```bash
python ./publisher/host_publisher.py
```


Good luck!
