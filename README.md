# MM802 Course Project
## Code Documents
- `packet.py`
- `client.py`
- `server.py`
- `link.py`
- `system.py`

## `packet.py`
A **class** that is representing a data packet. Including the following information:
- Packet size
- Packet checksum
- Packet serial number
- Packet loss (Yes or No)
- Current latency of the Packet

## `client.py`
A **class** that is mainly responsible for intimating behaviors of client side process. Including:
- Profiling servers and server clusters.
- Determining segmentation of data packets.
- Communicating with `server` object via `link` object.

## `server.py`
A **class** that is for intimating behaviors of server process. Including:
- Receiving the data packet from `client` side through `link` object
- Send `ACK` or `NO ACK` back to client through `link` object by checking:
    - Packet serial number (packet arriving order)
    - Packet checksum (correction of packet)
    - Packet loss (Too long delay)
- Initmating the **TCP** protocol

## `link.py`
A **class** that is intimating the behavior of intermediate packet transmission. Task including:
- Receiving the data packt from `client` object.
- Determining the probability of packet loss.
- Determining the time of delay (including congestion).
- Determining the probability of packet correction.
- Determining if sending data to `server` or not based on the packet loss.
- Sending data to server based on packet correction, packet loss rate and packet order

## `system.py`
A **script** that is responsible for arranging our simulation task.
