from typing import Iterator, List, Optional, Tuple, Union

from .types import (
    HTTPCookieMap,
    HTTPEncodableValue,
)


def map_cookie_value(cookie_value: Union[str, bytes]) -> HTTPEncodableValue:
    if isinstance(cookie_value, bytes):
        cookie_value = cookie_value.decode('utf-8', errors='replace')

    stripped = cookie_value.strip()
    lowered = stripped.lower()

    if lowered == 'true':
        return True
    if lowered == 'false':
        return False
    if lowered == 'none':
        return None

    try:
        return int(stripped)
    except ValueError:
        pass

    try:
        return float(stripped)
    except ValueError:
        return stripped


class Cookies:

    def __init__(self) -> None:
        self._data: bytes = b''
        self._split: Optional[List[List[bytes]]] = None
        self._parsed: Optional[HTTPCookieMap] = None

    def __getitem__(self, name: str) -> HTTPEncodableValue:
        return self.parsed.get(name)

    def __iter__(self) -> Iterator[Tuple[str, HTTPEncodableValue]]:
        for cookie_name, cookie_value in self.parsed.items():
            yield cookie_name, cookie_value

    def update(self, data: Union[str, bytes]) -> None:
        encoded = data.encode('utf-8') if isinstance(data, str) else data
        if not encoded:
            return
        if self._data and not self._data.rstrip().endswith(b';') and not encoded.lstrip().startswith(b';'):
            self._data += b'; ' + encoded
        else:
            self._data += encoded
        self._split = None
        self._parsed = None

    @property
    def parsed(self) -> HTTPCookieMap:
        if self._split is None:
            self._split = [
                cookie.split(b'=')
                for cookie in self._data.split(b';')
                if cookie.strip()
            ]

        if self._parsed is None:
            parsed: HTTPCookieMap = {}

            for cookie in self._split:
                cookie_name = cookie[0].decode('utf-8', errors='replace').strip()
                if not cookie_name:
                    continue

                if len(cookie) == 1:
                    parsed[cookie_name] = cookie_name
                elif len(cookie) == 2:
                    parsed[cookie_name] = map_cookie_value(cookie[1])
                else:
                    parsed[cookie_name] = map_cookie_value(b'='.join(cookie[1:]))

            self._parsed = parsed

        return self._parsed
