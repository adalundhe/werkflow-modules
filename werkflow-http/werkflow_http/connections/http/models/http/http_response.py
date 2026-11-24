import gzip
import re
from typing import Any, Dict, Literal, Optional, Type, TypeVar

import orjson
from pydantic import BaseModel, ConfigDict, Field, JsonValue, StrictBytes, StrictInt, StrictStr

from .cookies import Cookies
from .metadata import Metadata
from .url_metadata import URLMetadata

space_pattern = re.compile(r"\s+")

T = TypeVar('T', bound=BaseModel)


class HTTPResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    metadata: Optional[Metadata] = None
    url: URLMetadata
    method: Optional[
        Literal[
            "GET",
            "POST",
            "HEAD",
            "OPTIONS",
            "PUT",
            "PATCH",
            "DELETE",
        ]
    ] = None
    cookies: Optional[Cookies] = None
    status: Optional[StrictInt] = None
    status_message: Optional[StrictStr] = None
    headers: Dict[StrictBytes, StrictBytes] = Field(default_factory=dict)
    content: StrictBytes | bytearray = b''

    def check_success(self) -> bool:
        return self.status is not None and 200 <= self.status < 300

    def json(  # type: ignore[override]
        self,
        return_failures: bool = True,
    ) -> JsonValue | Exception:
        try:
            if self.content:
                raw = bytes(self.content) if isinstance(self.content, bytearray) else self.content
                return orjson.loads(raw)

            return {}

        except Exception as parse_error:
            if return_failures:
                return parse_error

            raise parse_error

    def text(
        self,
        encoding: str = 'utf-8',
        return_failures: bool = True,
    ) -> str | Exception:
        try:
            return self.content.decode(encoding=encoding)

        except Exception as parse_error:
            if return_failures:
                return parse_error

            raise parse_error

    def to_model(
        self,
        model: Type[T],
        return_failures: bool = True,
    ) -> T | Exception:
        try:
            raw = bytes(self.content) if isinstance(self.content, bytearray) else self.content
            return model(**orjson.loads(raw))

        except Exception as parse_error:
            if return_failures:
                return parse_error

            raise parse_error

    def unzip(
        self,
        return_failures: bool = True,
    ) -> bytes | Exception:
        try:
            return gzip.decompress(self.content)

        except Exception as parse_error:
            if return_failures:
                return parse_error

            raise parse_error

    @property
    def data(self) -> Any:
        return self.parse_data()

    def parse_data(
        self,
        model: Optional[Type[T]] = None,
        return_failures: bool = True,
    ) -> Any:
        if model is not None:
            return self.to_model(
                model,
                return_failures=return_failures,
            )

        raw_content_type = self.headers.get(b'content-type')
        content_type: bytes | None = None
        if raw_content_type is not None:
            content_type = raw_content_type.split(b';', 1)[0].strip().lower()

        try:
            match content_type:
                case b'application/json':
                    return self.json(return_failures=return_failures)
                case b'text/plain' | b'text/html' | b'text/csv':
                    return self.text(return_failures=return_failures)
                case b'application/gzip':
                    return self.unzip(return_failures=return_failures)
                case _:
                    return bytes(self.content) if isinstance(self.content, bytearray) else self.content

        except Exception:
            if not return_failures:
                raise
            return bytes(self.content) if isinstance(self.content, bytearray) else self.content
