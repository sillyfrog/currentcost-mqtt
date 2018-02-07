# currentcost-mqtt

By configuring your DNS server to redirect the following domains to the host
running this service, you can broadcast the data captured via MQTT.

Domains to redirect:
- www.pachube.com
- provisioning.connectedenvironments.com

You will also need to update the `BROKER` variable for your network.

The included `Dockerfile` is how I run it, but it is not required and can be run standalone.

This requires a http://currentcost.com/ device, and modification of DNS on
your network for this to work. This is especially helpful while
http://my.currentcost.com/ is migrated to a new server so you can still
capture your data.

If you wanted to send to something else, the senddata function can be
replaced with what ever works for you.
