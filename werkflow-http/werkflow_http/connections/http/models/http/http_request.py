import base64
import pathlib
from typing import Any, Dict, List, Literal, Optional, Sequence, Tuple, Union
from urllib.parse import urlencode

import orjson
from pydantic import (
    BaseModel,
    ConfigDict,
    InstanceOf,
    StrictBytes,
    StrictInt,
    StrictStr,
)

from .file import File
from .types import HTTPCookie, HTTPEncodableValue
from .url import URL

NEW_LINE = '\r\n'

HTTPMethod = Literal[
    "GET",
    "POST",
    "HEAD",
    "OPTIONS",
    "PUT",
    "PATCH",
    "DELETE",
]


class HTTPRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    url: StrictStr
    method: HTTPMethod
    cookies: Optional[List[HTTPCookie]] = None
    auth: Optional[Tuple[str, str]] = None
    params: Optional[Dict[str, HTTPEncodableValue]] = None
    headers: Optional[Dict[str, Union[int, float, str, bytes, None]]] = None
    data: Union[
        StrictStr,
        StrictBytes,
        Dict[str, Any],
        List[Any],
        InstanceOf[BaseModel],
        int,
        float,
        bool,
        None,
    ] = None
    files: Optional[Sequence[Union[File, StrictStr, pathlib.Path]]] = None
    redirects: StrictInt = 3

    def prepare_components(
        self,
        url: URL,
        encode_dict_body: bool = True,
    ) -> Tuple[str, Dict[str, str], Optional[bytes]]:
        url_path = url.path

        if self.params:
            filtered_params = {
                k: v for k, v in self.params.items() if v is not None
            }
            if filtered_params:
                url_params = urlencode(filtered_params)
                separator = '&' if '?' in url_path else '?'
                url_path += f'{separator}{url_params}'

        request_line = f"{self.method} {url_path} HTTP/1.1"

        port = url.port or (443 if url.is_ssl else 80)
        raw_hostname = url.hostname or ''
        hostname = raw_hostname.encode("idna").decode() if raw_hostname else ''

        if hostname and port not in (80, 443):
            hostname = f'{hostname}:{port}'

        user_headers: Dict[str, str] = {}
        if self.headers:
            for key, value in self.headers.items():
                if value is None:
                    continue
                if isinstance(value, bytes):
                    user_headers[key] = value.decode('latin-1')
                else:
                    user_headers[key] = str(value)

        lowered_user_keys = {k.lower() for k in user_headers}

        data: Optional[bytes] = None
        if isinstance(self.data, BaseModel):
            data = orjson.dumps(self.data.model_dump(mode='json', exclude_none=True))
            if 'content-type' not in lowered_user_keys:
                user_headers['Content-Type'] = 'application/json'
        elif isinstance(self.data, bytes):
            data = self.data
        elif isinstance(self.data, str):
            data = self.data.encode('utf-8')
        elif isinstance(self.data, (dict, list)):
            if encode_dict_body:
                data = orjson.dumps(self.data)
                if 'content-type' not in lowered_user_keys:
                    user_headers['Content-Type'] = 'application/json'
        elif self.data is not None:
            data = orjson.dumps(self.data)

        size = len(data) if data is not None else 0

        headers: Dict[str, str] = {}
        if 'host' not in lowered_user_keys and hostname:
            headers['Host'] = hostname
        if 'user-agent' not in lowered_user_keys:
            headers['User-Agent'] = 'mercury-http'
        if 'keep-alive' not in lowered_user_keys:
            headers['Keep-Alive'] = 'timeout=60, max=100000'
        if 'content-length' not in lowered_user_keys:
            headers['Content-Length'] = str(size)

        headers.update(user_headers)

        if self.auth and 'authorization' not in lowered_user_keys:
            encoded_auth_header = (
                base64.b64encode(f'{self.auth[0]}:{self.auth[1]}'.encode('utf-8'))
                .decode('ascii')
            )
            headers['Authorization'] = f'Basic {encoded_auth_header}'

        if self.cookies:
            cookie_parts: List[str] = []
            for cookie_data in self.cookies:
                if len(cookie_data) == 1:
                    cookie_parts.append(str(cookie_data[0]))
                elif len(cookie_data) == 2:
                    cookie_name, cookie_value = cookie_data
                    cookie_parts.append(f'{cookie_name}={cookie_value}')

            if cookie_parts:
                headers['Cookie'] = '; '.join(cookie_parts)

        return request_line, headers, data

    @staticmethod
    def serialize_headers(request_line: str, headers: Dict[str, str]) -> bytes:
        lines = [request_line]
        for key, value in headers.items():
            lines.append(f'{key}: {value}')
        return (NEW_LINE.join(lines) + NEW_LINE + NEW_LINE).encode('utf-8')

    def prepare(self, url: URL) -> Tuple[bytes, Optional[bytes]]:
        request_line, headers, data = self.prepare_components(url)
        return self.serialize_headers(request_line, headers), data
