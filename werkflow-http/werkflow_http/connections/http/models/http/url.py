import asyncio
import socket
from ipaddress import IPv4Address, ip_address
from typing import Iterator, List, Optional, Tuple
from urllib.parse import ParseResult, urlparse

import aiodns

from .types import SocketAddress, SocketConfig, SocketProtocols, SocketTypes


class URL:

    __slots__ = (
        'resolver',
        'ip_addr',
        'parsed',
        'is_ssl',
        'port',
        'full',
        'has_ip_addr',
        'socket_config',
        'family',
        'protocol',
        'loop',
        'ip_addresses',
        'address',
    )

    def __init__(
        self,
        url: str,
        port: int = 80,
        family: int = SocketTypes.DEFAULT,
        protocol: int = SocketProtocols.DEFAULT,
    ) -> None:
        self.resolver: Optional[aiodns.DNSResolver] = None
        self.ip_addr: Optional[str] = None
        self.parsed: ParseResult = urlparse(url)
        self.is_ssl: bool = self.parsed.scheme.lower() in ('https', 'wss')

        default_port = 443 if self.is_ssl else port
        self.port: int = self.parsed.port if self.parsed.port else default_port
        self.full: str = url
        self.has_ip_addr: bool = False
        self.family: int = family
        self.protocol: int = protocol
        self.loop: Optional[asyncio.AbstractEventLoop] = None
        self.ip_addresses: List[Tuple[str, SocketConfig]] = []
        self.address: Optional[str] = None
        self.socket_config: Optional[SocketConfig] = None

    async def replace(self, url: str) -> None:
        self.full = url
        self.parsed = urlparse(url)
        self.is_ssl = self.parsed.scheme.lower() in ('https', 'wss')
        default_port = 443 if self.is_ssl else 80
        self.port = self.parsed.port if self.parsed.port else default_port

    def __iter__(self) -> Iterator[Tuple[str, SocketConfig]]:
        for ip_info in self.ip_addresses:
            yield ip_info

    def update(
        self,
        url: str,
        port: int = 80,
        family: int = SocketTypes.DEFAULT,
        protocol: int = SocketProtocols.DEFAULT,
    ) -> None:
        self.parsed = urlparse(url)
        self.is_ssl = self.parsed.scheme.lower() in ('https', 'wss')

        default_port = 443 if self.is_ssl else port
        self.port = self.parsed.port if self.parsed.port else default_port
        self.full = url
        self.has_ip_addr = False
        self.socket_config = None
        self.family = family
        self.protocol = protocol
        self.loop = None
        self.ip_addresses = []
        self.address = None

    def _build_socket_entry(self, host: str) -> Tuple[str, SocketConfig]:
        parsed_ip = ip_address(host)
        if isinstance(parsed_ip, IPv4Address):
            socket_family = socket.AF_INET
            address_info: SocketAddress = (host, self.port)
        else:
            socket_family = socket.AF_INET6
            address_info = (host, self.port, 0, 0)

        return (
            host,
            (
                socket_family,
                self.protocol,
                0,
                '',
                address_info,
            ),
        )

    async def lookup(self) -> None:
        if self.loop is None:
            self.loop = asyncio.get_running_loop()

        self.ip_addresses = []

        if self.parsed.hostname is None:
            raw = self.full
            if raw.startswith('[') and ']:' in raw:
                host, port_str = raw[1:].rsplit(']:', 1)
            else:
                host, port_str = raw.rsplit(':', 1)

            self.port = int(port_str)
            self.ip_addresses = [self._build_socket_entry(host)]
            self.has_ip_addr = True
            return

        hostname = self.parsed.hostname
        try:
            ip_address(hostname)
        except ValueError:
            pass
        else:
            self.ip_addresses = [self._build_socket_entry(hostname)]
            self.has_ip_addr = True
            return

        if self.resolver is None:
            self.resolver = aiodns.DNSResolver(loop=self.loop)

        try:
            resolved = await self.resolver.gethostbyname(
                hostname,
                socket.AddressFamily(self.family),
            )
            addresses = list(resolved.addresses)
        except Exception:
            addr_infos = await self.loop.getaddrinfo(
                hostname,
                self.port,
                family=self.family,
                type=self.protocol,
            )
            addresses = []
            for info in addr_infos:
                addr_host = str(info[4][0])
                if addr_host not in addresses:
                    addresses.append(addr_host)

        for address in addresses:
            self.ip_addresses.append(self._build_socket_entry(address))

    def _replace_hostname(self, value: str) -> None:
        host_part = f'[{value}]' if (':' in value and not value.startswith('[')) else value
        if self.parsed.port is not None:
            netloc = f'{host_part}:{self.parsed.port}'
        else:
            netloc = host_part

        if self.parsed.username is not None:
            userinfo = self.parsed.username
            if self.parsed.password is not None:
                userinfo = f'{userinfo}:{self.parsed.password}'
            netloc = f'{userinfo}@{netloc}'

        self.parsed = self.parsed._replace(netloc=netloc)

    @property
    def params(self) -> str:
        return self.parsed.params

    @params.setter
    def params(self, value: str) -> None:
        self.parsed = self.parsed._replace(params=value)

    @property
    def scheme(self) -> str:
        return self.parsed.scheme

    @scheme.setter
    def scheme(self, value: str) -> None:
        self.parsed = self.parsed._replace(scheme=value)
        self.is_ssl = self.parsed.scheme.lower() in ('https', 'wss')

    @property
    def hostname(self) -> Optional[str]:
        return self.parsed.hostname

    @hostname.setter
    def hostname(self, value: str) -> None:
        self._replace_hostname(value)

    @property
    def path(self) -> str:
        url_path = self.parsed.path
        url_query = self.parsed.query
        url_params = self.parsed.params

        if not url_path:
            url_path = '/'

        if url_query:
            url_path += f'?{url_query}'
        elif url_params:
            url_path += f';{url_params}'

        return url_path

    @path.setter
    def path(self, value: str) -> None:
        self.parsed = self.parsed._replace(path=value)

    @property
    def query(self) -> str:
        return self.parsed.query

    @query.setter
    def query(self, value: str) -> None:
        self.parsed = self.parsed._replace(query=value)

    @property
    def authority(self) -> Optional[str]:
        return self.parsed.hostname

    @authority.setter
    def authority(self, value: str) -> None:
        self._replace_hostname(value)
