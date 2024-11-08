import gzip
import re
from typing import Dict, Literal, Optional, Type, TypeVar, Union

import orjson
from pydantic import BaseModel, Json, StrictBytes, StrictInt, StrictStr

from .cookies import Cookies
from .url_metadata import URLMetadata

space_pattern = re.compile(r"\s+")


T = TypeVar('T', bound=BaseModel)


class HTTPResponse(BaseModel):
    url: URLMetadata
    method: Optional[
        Literal[
            "GET", 
            "POST",
            "HEAD",
            "OPTIONS", 
            "PUT", 
            "PATCH", 
            "DELETE"
        ]
    ]=None
    cookies: Union[
        Optional[Cookies],
        Optional[None]
    ]=None
    status: Optional[StrictInt]=None
    status_message: Optional[StrictStr]=None
    headers: Dict[StrictBytes, StrictBytes]={}
    content: StrictBytes | bytearray=b''

    class Config:
        arbitrary_types_allowed=True

    def check_success(self) -> bool:
        return (
            self.status and self.status >= 200 and self.status < 300
        )
    
    def json(
        self,
        return_failures: bool = True,
    ) -> Json | Exception:

        try:
            if self.content:
                return orjson.loads(
                    self.content
                )
        
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
            return self.content.decode(
                encoding=encoding,
            )
        
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
            return model(**orjson.loads(
                self.content
            ))
        
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
    def data(
        self,
        model: Optional[Type[T]]=None,
        return_failures: bool = True
    ):

        content_type = self.headers.get('content-type')

        if model:
            return self.to_model(
                model,
                return_failures=return_failures,
            )

        try:
            match content_type:

                case 'application/json':
                    return self.json(
                        return_failures=return_failures,
                    )
                
                case 'text/plain':
                    return self.text()
                
                case 'application/gzip':
                    return self.unzip(
                        return_failures=return_failures,
                    )
                
                case _:
                    return self.content

        except Exception:
            return self.content
            
 