import socket
from typing import Dict, Optional, Tuple, Union

HTTPEncodableValue = Union[
    str,
    int,
    float,
    bool,
    None,
]

HTTPCookie = Union[Tuple[str], Tuple[str, HTTPEncodableValue]]
HTTPCookieMap = Dict[str, HTTPEncodableValue]
SocketAddress = Union[Tuple[str, int], Tuple[str, int, int, int]]
SocketConfig = Tuple[int, int, int, str, SocketAddress]


class SocketTypes:
    DEFAULT = socket.AF_INET
    HTTP2 = socket.AF_INET
    UDP = socket.AF_INET
    HTTP3 = socket.AF_INET6
    NONE = None


class SocketProtocols:
    DEFAULT = socket.SOCK_STREAM
    HTTP2 = socket.SOCK_STREAM
    HTTP3 = socket.SOCK_DGRAM
    UDP = socket.SOCK_DGRAM
    NONE = None


class RequestTypes:
    HTTP = 'HTTP'
    HTTP2 = 'HTTP2'
    HTTP3 = 'HTTP3'
    WEBSOCKET = 'WEBSOCKET'
    GRAPHQL = 'GRAPHQL'
    GRAPHQL_HTTP2 = 'GRAPHQL_HTTP2'
    GRPC = 'GRPC'
    PLAYWRIGHT = 'PLAYWRIGHT'
    UDP = 'UDP'
    TASK = 'TASK'
    CUSTOM = 'CUSTOM'


class ProtocolMap:

    def __init__(self) -> None:
        self.address_families: Dict[str, Optional[socket.AddressFamily]] = {
            RequestTypes.HTTP: SocketTypes.DEFAULT,
            RequestTypes.HTTP2: SocketTypes.HTTP2,
            RequestTypes.HTTP3: SocketTypes.HTTP3,
            RequestTypes.WEBSOCKET: SocketTypes.DEFAULT,
            RequestTypes.GRAPHQL: SocketTypes.DEFAULT,
            RequestTypes.GRAPHQL_HTTP2: SocketTypes.HTTP2,
            RequestTypes.GRPC: SocketTypes.HTTP2,
            RequestTypes.UDP: SocketTypes.UDP,
        }

        self.protocols: Dict[str, Optional[socket.SocketKind]] = {
            RequestTypes.HTTP: SocketProtocols.DEFAULT,
            RequestTypes.HTTP2: SocketProtocols.HTTP2,
            RequestTypes.HTTP3: SocketProtocols.HTTP3,
            RequestTypes.WEBSOCKET: SocketProtocols.DEFAULT,
            RequestTypes.GRAPHQL: SocketProtocols.DEFAULT,
            RequestTypes.GRAPHQL_HTTP2: SocketProtocols.HTTP2,
            RequestTypes.GRPC: SocketProtocols.HTTP2,
            RequestTypes.UDP: SocketProtocols.UDP,
        }

    def __getitem__(
        self,
        key: str,
    ) -> Tuple[Optional[socket.AddressFamily], Optional[socket.SocketKind]]:
        return self.address_families.get(key), self.protocols.get(key)
