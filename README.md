# currentcost-mqtt

By configuring your DNS server to redirect the following domains to the host
running this service, you can broadcast the data captured via MQTT.

Hostnames to redirect:
- www.pachube.com
- api.pachube.com
- provisioning.connectedenvironments.com

You will also need to update the `BROKER` and `PORT` variables to point to your MQTT broker.

The included `Dockerfile` is how I run it, but it is not required and can be run standalone.

This requires a http://currentcost.com/ device, and modification of DNS on
your network for this to work.

The http://my.currentcost.com dashboard no longer works. It relied on 'Xively Personal' and LogMeIn retired
the Xively Personal product on January 15, 2018.

If you wanted to send to something else, the senddata function can be
replaced with what ever works for you.
