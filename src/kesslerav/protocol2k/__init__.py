"""
Encapsulates Protocol 2000 communication and devices
"""
from typing import Optional

from ..media_switch import MediaSwitch as MediaSwitchProtocol
from .io import TcpDevice, TcpEndpoint, SerialDevice, SerialEndpoint
from .media_switch import MediaSwitch


def get_tcp_media_switch(
    host: str,
    port: Optional[int] = None,
    timeout_sec: Optional[float] = None,
    machine_id: Optional[int] = None
) -> MediaSwitchProtocol:
    if timeout_sec is None:
        # Let `TcpEndpoint` manage timeout
        endpoint = TcpEndpoint(host, port)
    else:
        endpoint = TcpEndpoint(host, port, timeout_sec)
    tcp_device = TcpDevice(endpoint)
    return MediaSwitch(tcp_device, machine_id)


def get_serial_media_switch(
    port,
    timeout_sec: Optional[float] = None,
    machine_id: Optional[int] = None
) -> MediaSwitchProtocol:
    if timeout_sec is None:
        endpoint = SerialEndpoint(port)
    else:
        endpoint = SerialEndpoint(port, timeout_sec)
    serial_device = SerialDevice(endpoint)
    return MediaSwitch(serial_device, machine_id)
