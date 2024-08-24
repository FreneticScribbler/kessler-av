"""
Encapsulates Protocol 2000 communication and devices
"""
from typing import Optional

from ..media_switch import MediaSwitch as MediaSwitchProtocol
from .io import TcpDevice, TcpEndpoint, SerialDevice, SerialEndpoint, Instruction, Command
from .media_switch import MediaSwitch, MediaMatrix


def get_switch_or_matrix(connection_device, machine_id):
    # Need to know output count early when setting up matrix, so get it here
    output_count = connection_device.process(Instruction(Command.DEFINE_MACHINE, 2, 1, machine_id))[0].output_value
    if output_count > 1:
        return MediaMatrix(connection_device, output_count, machine_id)
    else:
        return MediaSwitch(connection_device, machine_id)

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
    return get_switch_or_matrix(tcp_device, machine_id)


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
    return get_switch_or_matrix(serial_device, machine_id)
