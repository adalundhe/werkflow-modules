from __future__ import annotations

import asyncio
import binascii
import pathlib
import secrets
import ssl
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from typing import (
    Any,
    Dict,
    List,
    Literal,
    Optional,
    Sequence,
    Tuple,
    Union,
)
from urllib.parse import urljoin, urlparse

from pydantic import BaseModel

from .models.http import (
    URL,
    Cookies,
    File,
    HTTPCookie,
    HTTPEncodableValue,
    HTTPRequest,
    HTTPResponse,
    Metadata,
    URLMetadata,
)
from .protocols import HTTPConnection
from .timeouts import Timeouts

HTTPMethod = Literal[
    "GET",
    "POST",
    "HEAD",
    "OPTIONS",
    "PUT",
    "PATCH",
    "DELETE",
]
URLCacheKey = Tuple[str, str, int]
REDIRECT_STATUSES = frozenset({301, 302, 303, 307, 308})


class MercurySyncHTTPConnection:

    def __init__(
        self,
        cert_path: Optional[str] = None,
        key_path: Optional[str] = None,
        pool_size: Optional[int] = None,
        verify_ssl: bool = True,
    ) -> None:
        if pool_size is None:
            pool_size = 100

        self.timeouts = Timeouts()

        self._cert_path = cert_path
        self._key_path = key_path
        self._verify_ssl = verify_ssl
        self._client_ssl_context = self._create_general_client_ssl_context(
            cert_path=cert_path,
            key_path=key_path,
        )

        self._dns_lock: Dict[URLCacheKey, asyncio.Lock] = defaultdict(asyncio.Lock)
        self._connections: List[HTTPConnection] = [
            HTTPConnection() for _ in range(pool_size)
        ]

        self._max_concurrency = pool_size
        self._semaphore = asyncio.Semaphore(self._max_concurrency)
        self._url_cache: Dict[URLCacheKey, URL] = {}

    def _create_general_client_ssl_context(
        self,
        cert_path: Optional[str] = None,
        key_path: Optional[str] = None,
    ) -> ssl.SSLContext:
        ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        if cert_path and key_path:
            ctx.load_cert_chain(certfile=cert_path, keyfile=key_path)
        if not self._verify_ssl:
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
        return ctx

    def _get_ssl_context(
        self,
        cert_path: Optional[str] = None,
        key_path: Optional[str] = None,
    ) -> ssl.SSLContext:
        if cert_path != self._cert_path or key_path != self._key_path:
            return self._create_general_client_ssl_context(
                cert_path=cert_path,
                key_path=key_path,
            )
        return self._client_ssl_context

    @staticmethod
    def _encode_headers_dict(
        headers: Optional[Dict[str, Any]],
    ) -> Dict[bytes, bytes]:
        encoded: Dict[bytes, bytes] = {}
        if not headers:
            return encoded
        for key, value in headers.items():
            if value is None:
                continue
            key_bytes = key if isinstance(key, bytes) else str(key).encode('utf-8')
            val_bytes = value if isinstance(value, bytes) else str(value).encode('utf-8')
            encoded[key_bytes.lower()] = val_bytes
        return encoded

    def _build_timeout_response(
        self,
        url: str,
        method: HTTPMethod,
        headers: Optional[Dict[str, Any]] = None,
    ) -> HTTPResponse:
        url_data = urlparse(url)
        return HTTPResponse(
            metadata=Metadata(),
            url=URLMetadata(
                host=url_data.hostname,
                path=url_data.path or '/',
                params=url_data.params or None,
                query=url_data.query or None,
            ),
            headers=self._encode_headers_dict(headers),
            method=method,
            status=408,
            status_message='Request timed out.',
        )

    async def head(
        self,
        url: str,
        auth: Optional[Tuple[str, str]] = None,
        cookies: Optional[List[HTTPCookie]] = None,
        headers: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, HTTPEncodableValue]] = None,
        timeout: Optional[Union[int, float]] = None,
        redirects: int = 3,
    ) -> HTTPResponse:
        async with self._semaphore:
            try:
                return await asyncio.wait_for(
                    self._request(
                        HTTPRequest(
                            url=url,
                            method='HEAD',
                            cookies=cookies,
                            auth=auth,
                            headers=headers,
                            params=params,
                            redirects=redirects,
                        ),
                    ),
                    timeout=timeout,
                )
            except asyncio.TimeoutError:
                return self._build_timeout_response(url, 'HEAD', headers)

    async def options(
        self,
        url: str,
        auth: Optional[Tuple[str, str]] = None,
        cookies: Optional[List[HTTPCookie]] = None,
        headers: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, HTTPEncodableValue]] = None,
        timeout: Optional[Union[int, float]] = None,
        redirects: int = 3,
    ) -> HTTPResponse:
        async with self._semaphore:
            try:
                return await asyncio.wait_for(
                    self._request(
                        HTTPRequest(
                            url=url,
                            method='OPTIONS',
                            cookies=cookies,
                            auth=auth,
                            headers=headers,
                            params=params,
                            redirects=redirects,
                        ),
                    ),
                    timeout=timeout,
                )
            except asyncio.TimeoutError:
                return self._build_timeout_response(url, 'OPTIONS', headers)

    async def get(
        self,
        url: str,
        auth: Optional[Tuple[str, str]] = None,
        cookies: Optional[List[HTTPCookie]] = None,
        headers: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, HTTPEncodableValue]] = None,
        timeout: Optional[Union[int, float]] = None,
        redirects: int = 3,
    ) -> HTTPResponse:
        async with self._semaphore:
            try:
                return await asyncio.wait_for(
                    self._request(
                        HTTPRequest(
                            url=url,
                            method='GET',
                            cookies=cookies,
                            data=None,
                            auth=auth,
                            headers=headers,
                            params=params,
                            redirects=redirects,
                        )
                    ),
                    timeout=timeout,
                )
            except asyncio.TimeoutError:
                return self._build_timeout_response(url, 'GET', headers)

    async def post(
        self,
        url: str,
        auth: Optional[Tuple[str, str]] = None,
        cookies: Optional[List[HTTPCookie]] = None,
        headers: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, HTTPEncodableValue]] = None,
        timeout: Optional[Union[int, float]] = None,
        data: Any = None,
        files: Optional[Sequence[Union[File, str, pathlib.Path]]] = None,
        redirects: int = 3,
    ) -> HTTPResponse:
        async with self._semaphore:
            try:
                return await asyncio.wait_for(
                    self._request(
                        HTTPRequest(
                            url=url,
                            method='POST',
                            cookies=cookies,
                            auth=auth,
                            headers=headers,
                            params=params,
                            data=data,
                            files=files,
                            redirects=redirects,
                        ),
                    ),
                    timeout=timeout,
                )
            except asyncio.TimeoutError:
                return self._build_timeout_response(url, 'POST', headers)

    async def put(
        self,
        url: str,
        auth: Optional[Tuple[str, str]] = None,
        cookies: Optional[List[HTTPCookie]] = None,
        headers: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, HTTPEncodableValue]] = None,
        timeout: Optional[Union[int, float]] = None,
        data: Any = None,
        files: Optional[Sequence[Union[File, str, pathlib.Path]]] = None,
        redirects: int = 3,
    ) -> HTTPResponse:
        async with self._semaphore:
            try:
                return await asyncio.wait_for(
                    self._request(
                        HTTPRequest(
                            url=url,
                            method='PUT',
                            cookies=cookies,
                            auth=auth,
                            headers=headers,
                            params=params,
                            data=data,
                            files=files,
                            redirects=redirects,
                        ),
                    ),
                    timeout=timeout,
                )
            except asyncio.TimeoutError:
                return self._build_timeout_response(url, 'PUT', headers)

    async def patch(
        self,
        url: str,
        auth: Optional[Tuple[str, str]] = None,
        cookies: Optional[List[HTTPCookie]] = None,
        headers: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, HTTPEncodableValue]] = None,
        timeout: Optional[Union[int, float]] = None,
        data: Any = None,
        files: Optional[Sequence[Union[File, str, pathlib.Path]]] = None,
        redirects: int = 3,
    ) -> HTTPResponse:
        async with self._semaphore:
            try:
                return await asyncio.wait_for(
                    self._request(
                        HTTPRequest(
                            url=url,
                            method='PATCH',
                            cookies=cookies,
                            auth=auth,
                            headers=headers,
                            params=params,
                            data=data,
                            files=files,
                            redirects=redirects,
                        ),
                    ),
                    timeout=timeout,
                )
            except asyncio.TimeoutError:
                return self._build_timeout_response(url, 'PATCH', headers)

    async def delete(
        self,
        url: str,
        auth: Optional[Tuple[str, str]] = None,
        cookies: Optional[List[HTTPCookie]] = None,
        headers: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, HTTPEncodableValue]] = None,
        timeout: Optional[Union[int, float]] = None,
        redirects: int = 3,
    ) -> HTTPResponse:
        async with self._semaphore:
            try:
                return await asyncio.wait_for(
                    self._request(
                        HTTPRequest(
                            url=url,
                            method='DELETE',
                            cookies=cookies,
                            auth=auth,
                            headers=headers,
                            params=params,
                            redirects=redirects,
                        ),
                    ),
                    timeout=timeout,
                )
            except asyncio.TimeoutError:
                return self._build_timeout_response(url, 'DELETE', headers)

    async def _request(
        self,
        request: HTTPRequest,
        cert_path: Optional[str] = None,
        key_path: Optional[str] = None,
    ) -> HTTPResponse:
        if cert_path is None:
            cert_path = self._cert_path

        if key_path is None:
            key_path = self._key_path

        current_url = request.url
        result, redirect = await self._execute(
            request,
            cert_path=cert_path,
            key_path=key_path,
        )

        if redirect and request.redirects > 0:
            for _ in range(request.redirects):
                raw_location = result.headers.get(b'location')
                if raw_location is None:
                    break

                location = urljoin(
                    current_url,
                    raw_location.decode('utf-8', errors='replace').strip(),
                )
                target_scheme = urlparse(location).scheme.lower()
                source_scheme = urlparse(current_url).scheme.lower()
                upgrade_ssl = target_scheme == 'https' and source_scheme != 'https'

                current_url = location
                result, redirect = await self._execute(
                    request,
                    upgrade_ssl=upgrade_ssl,
                    redirect_url=location,
                    cert_path=cert_path,
                    key_path=key_path,
                )

                if not redirect:
                    break

        return result

    async def _execute(
        self,
        request: HTTPRequest,
        upgrade_ssl: bool = False,
        redirect_url: Optional[str] = None,
        cert_path: Optional[str] = None,
        key_path: Optional[str] = None,
    ) -> Tuple[HTTPResponse, bool]:
        request_url = redirect_url if redirect_url else request.url
        connection: Optional[HTTPConnection] = None
        connection_healthy = False

        try:
            connection, url, should_upgrade_ssl = await asyncio.wait_for(
                self._connect_to_url_location(
                    request_url,
                    ssl_redirect_url=request_url if upgrade_ssl else None,
                    cert_path=cert_path,
                    key_path=key_path,
                ),
                timeout=self.timeouts.connect_timeout,
            )

            if should_upgrade_ssl:
                ssl_redirect_url = request_url.replace('http://', 'https://', 1)
                connection, url, _ = await asyncio.wait_for(
                    self._connect_to_url_location(
                        request_url,
                        ssl_redirect_url=ssl_redirect_url,
                        cert_path=cert_path,
                        key_path=key_path,
                    ),
                    timeout=self.timeouts.connect_timeout,
                )
                request_url = ssl_redirect_url

            if connection is None:
                raise ConnectionError(f'Unable to connect to {request_url}')

            if request.files:
                request_line, request_headers, prepared_body = request.prepare_components(
                    url,
                    encode_dict_body=False,
                )
                upload_body: Any = (
                    request.data
                    if isinstance(request.data, dict)
                    else prepared_body
                )
                updated_headers, data, err = await self._upload_files(
                    request.files,
                    upload_body,
                    request_headers,
                )
                if err is not None or updated_headers is None:
                    connection_healthy = True
                    return HTTPResponse(
                        metadata=Metadata(),
                        url=URLMetadata(
                            host=url.hostname,
                            path=url.path,
                        ),
                        method=request.method,
                        status=400,
                        status_message=str(err) if err is not None else 'File upload failed.',
                        headers=self._encode_headers_dict(request_headers),
                    ), False

                raw_headers = request.serialize_headers(request_line, updated_headers)
                response_err_headers = self._encode_headers_dict(updated_headers)
            else:
                raw_headers, data = request.prepare(url)
                response_err_headers = self._encode_headers_dict(request.headers)

            if connection.reader is None:
                return HTTPResponse(
                    metadata=Metadata(),
                    url=URLMetadata(
                        host=url.hostname,
                        path=url.path,
                    ),
                    method=request.method,
                    status=400,
                    status_message='Connection reader is unavailable.',
                    headers=response_err_headers,
                ), False

            connection.write(raw_headers)
            if data:
                connection.write(data)

            response_code = await asyncio.wait_for(
                connection.reader.readline(),
                timeout=self.timeouts.read_timeout,
            )
            if not response_code:
                raise ConnectionError('Connection closed before receiving HTTP status line.')

            response_headers: Dict[bytes, bytes] = await asyncio.wait_for(
                connection.read_headers(),
                timeout=self.timeouts.read_timeout,
            )

            status_parts: List[bytes] = response_code.split()
            if len(status_parts) < 2:
                raise ValueError(f'Malformed HTTP status line: {response_code!r}')

            status = int(status_parts[1])
            status_message = (
                b' '.join(status_parts[2:]).decode('utf-8', errors='replace')
                if len(status_parts) > 2
                else None
            )

            content_length = response_headers.get(b'content-length')
            transfer_encoding = response_headers.get(b'transfer-encoding')
            connection_header = response_headers.get(b'connection', b'').lower()
            server_closes = b'close' in connection_header

            if status in REDIRECT_STATUSES and b'location' in response_headers:
                if not content_length and not transfer_encoding and not server_closes:
                    connection_healthy = True
                return HTTPResponse(
                    metadata=Metadata(),
                    url=URLMetadata(
                        host=url.hostname,
                        path=url.path,
                    ),
                    method=request.method,
                    status=status,
                    status_message=status_message,
                    headers=response_headers,
                ), True

            cookies: Optional[Cookies] = None
            cookies_data: Optional[bytes] = response_headers.get(b'set-cookie')
            if cookies_data:
                cookies = Cookies()
                cookies.update(cookies_data)

            body: Union[bytes, bytearray] = b''
            has_no_body = (
                request.method == 'HEAD'
                or status in (204, 304)
                or (100 <= status < 200)
            )

            if not has_no_body:
                if content_length is not None:
                    length = int(content_length.strip())
                    if length > 0:
                        body = await asyncio.wait_for(
                            connection.readexactly(length),
                            timeout=self.timeouts.read_timeout,
                        )
                elif transfer_encoding is not None and b'chunked' in transfer_encoding.lower():
                    body = bytearray()
                    while True:
                        chunk_size_line = await asyncio.wait_for(
                            connection.readline(),
                            timeout=self.timeouts.read_timeout,
                        )
                        if not chunk_size_line:
                            break
                        chunk_size_hex = chunk_size_line.split(b';', 1)[0].strip()
                        chunk_size = int(chunk_size_hex, 16)
                        if chunk_size == 0:
                            # Consume trailing headers/CRLF until empty line
                            while True:
                                trailer = await asyncio.wait_for(
                                    connection.readline(),
                                    timeout=self.timeouts.read_timeout,
                                )
                                if not trailer or trailer in (b'\r\n', b'\n'):
                                    break
                            break

                        chunk = await asyncio.wait_for(
                            connection.readexactly(chunk_size + 2),
                            timeout=self.timeouts.read_timeout,
                        )
                        body.extend(chunk[:-2])

            connection_healthy = not server_closes

            return HTTPResponse(
                metadata=Metadata(),
                url=URLMetadata(
                    host=url.hostname,
                    path=url.path,
                ),
                cookies=cookies,
                method=request.method,
                status=status,
                status_message=status_message,
                headers=response_headers,
                content=bytes(body),
            ), False

        except Exception as request_exception:
            parsed_err_url = urlparse(request_url)
            return HTTPResponse(
                metadata=Metadata(),
                url=URLMetadata(
                    host=parsed_err_url.hostname,
                    path=parsed_err_url.path or '/',
                ),
                method=request.method,
                status=400,
                status_message=str(request_exception),
                headers={},
            ), False

        finally:
            if connection is not None:
                if connection_healthy:
                    self._connections.append(connection)
                else:
                    try:
                        await connection.close()
                    except Exception:
                        pass
                    self._connections.append(HTTPConnection())

    async def _upload_files(
        self,
        files: Sequence[Union[File, str, pathlib.Path]],
        body: Any,
        headers: Dict[str, str],
    ) -> Tuple[Optional[Dict[str, str]], Optional[bytes], Optional[Exception]]:
        executor = ThreadPoolExecutor(
            max_workers=max(1, len(files)),
        )

        try:
            completed: List[Union[File, Exception]] = []
            for file in files:
                try:
                    if isinstance(file, File) and file.data is None:
                        if file.path is None:
                            raise ValueError('File must specify either data or path.')
                        completed.append(
                            await File.upload(
                                file.path,
                                name=file.name,
                                content_type=file.content_type,
                                mode=file.mode,
                                executor=executor,
                            )
                        )
                    elif isinstance(file, (str, pathlib.Path)):
                        completed.append(
                            await File.upload(
                                str(file),
                                executor=executor,
                            )
                        )
                    else:
                        completed.append(file)
                except Exception as file_err:
                    completed.append(file_err)

            uploaded_files: List[File] = []
            for item in completed:
                if isinstance(item, Exception):
                    return None, None, item
                uploaded_files.append(item)

            boundary = binascii.hexlify(secrets.token_bytes(16)).decode('ascii')
            boundary_line = f'--{boundary}\r\n'.encode('latin-1')
            closing_boundary = f'--{boundary}--\r\n'.encode('latin-1')

            buffer = bytearray()

            if isinstance(body, dict):
                for field_name, field_value in body.items():
                    if field_value is None:
                        continue
                    buffer.extend(boundary_line)
                    buffer.extend(
                        f'Content-Disposition: form-data; name="{field_name}"\r\n\r\n'.encode('utf-8')
                    )
                    if isinstance(field_value, bytes):
                        buffer.extend(field_value)
                    else:
                        buffer.extend(str(field_value).encode('utf-8'))
                    buffer.extend(b'\r\n')
            elif isinstance(body, (bytes, bytearray)) and len(body) > 0:
                buffer.extend(boundary_line)
                buffer.extend(
                    b'Content-Disposition: form-data; name="data"\r\n\r\n'
                )
                buffer.extend(body)
                buffer.extend(b'\r\n')

            for uploaded_file in uploaded_files:
                file_headers = uploaded_file.to_headers()
                encoded_part_headers = '\r\n'.join(
                    f'{key}: {value}'
                    for key, value in file_headers.items()
                ).encode('utf-8')

                file_data = uploaded_file.to_data() or b''

                buffer.extend(boundary_line)
                buffer.extend(encoded_part_headers)
                buffer.extend(b'\r\n\r\n')
                buffer.extend(file_data)
                buffer.extend(b'\r\n')

            buffer.extend(closing_boundary)

            updated_headers: Dict[str, str] = {
                k: v
                for k, v in headers.items()
                if k.lower() not in ('content-type', 'content-length')
            }
            updated_headers['Content-Type'] = f'multipart/form-data; boundary={boundary}'
            updated_headers['Content-Length'] = str(len(buffer))

            return updated_headers, bytes(buffer), None

        except Exception as err:
            return None, None, err

        finally:
            executor.shutdown(wait=False)

    async def _connect_to_url_location(
        self,
        request_url: str,
        ssl_redirect_url: Optional[str] = None,
        cert_path: Optional[str] = None,
        key_path: Optional[str] = None,
    ) -> Tuple[Optional[HTTPConnection], URL, bool]:
        target_url_str = ssl_redirect_url if ssl_redirect_url else request_url
        parsed_url = URL(target_url_str)

        cache_key: URLCacheKey = (
            parsed_url.scheme.lower(),
            parsed_url.hostname or parsed_url.full,
            parsed_url.port,
        )
        url = self._url_cache.get(cache_key)
        do_dns_lookup = url is None or ssl_redirect_url is not None

        if do_dns_lookup:
            dns_lock = self._dns_lock[cache_key]
            async with dns_lock:
                url = self._url_cache.get(cache_key)
                if url is None or ssl_redirect_url is not None:
                    url = parsed_url
                    await url.lookup()
                    self._url_cache[cache_key] = url

        assert url is not None
        connection = self._connections.pop() if self._connections else HTTPConnection()
        ssl_context = (
            self._get_ssl_context(cert_path=cert_path, key_path=key_path)
            if (url.is_ssl or ssl_redirect_url is not None)
            else None
        )

        if url.address is None or url.socket_config is None or ssl_redirect_url is not None:
            connected = False
            last_error: Optional[Exception] = None

            for address, ip_info in url:
                try:
                    await connection.make_connection(
                        url.hostname or address,
                        address,
                        url.port,
                        ip_info,
                        ssl=ssl_context,
                        ssl_upgrade=ssl_redirect_url is not None,
                    )
                    url.address = address
                    url.socket_config = ip_info
                    connected = True
                    break
                except Exception as connection_error:
                    if 'server_hostname is only meaningful with ssl' in str(connection_error):
                        self._connections.append(connection)
                        return None, parsed_url, True
                    last_error = connection_error

            if not connected:
                self._connections.append(connection)
                raise last_error or ConnectionError(f'Unable to connect to {url.full}')
        else:
            try:
                await connection.make_connection(
                    url.hostname or url.address,
                    url.address,
                    url.port,
                    url.socket_config,
                    ssl=ssl_context,
                    ssl_upgrade=False,
                )
            except Exception as connection_error:
                self._connections.append(connection)
                if 'server_hostname is only meaningful with ssl' in str(connection_error):
                    return None, parsed_url, True
                raise

        return connection, parsed_url, False

    def abort(self) -> None:
        for conn in self._connections:
            conn.abort()

    async def close(self) -> None:
        await asyncio.gather(
            *(conn.close() for conn in self._connections),
            return_exceptions=True,
        )
