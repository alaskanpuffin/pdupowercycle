# PDU Power Cycle Script/Docker Container

The script is configured using the following enviroment variables.

`HOST` - The host being monitored. When this host goes down, the PDU will power cycle the socket listed below.

`PDU_HOST` - The network connected PDU's IP address.

`PDU_SOCKET` - The electric socket number that you want to restart on the PDU.

`PDU_USERNAME` - Username to sign into the PDU.

`PDU_PASSWORD` - Password for the above user.

Docker Container Available Here: https://hub.docker.com/r/alaskanpuffin/pdupowercycle
