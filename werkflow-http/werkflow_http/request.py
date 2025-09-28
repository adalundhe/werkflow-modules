from typing import Dict, List, Tuple, Union

from pydantic import BaseModel, StrictStr
from .connections.http.models.http import File as File

Headers = Dict[str, Union[int, float, str, bytes, None]]
Params = Dict[str, str]


JSONEncodable = str | bool | int | float | None
Data = JSONEncodable | List[JSONEncodable] | Dict[JSONEncodable, JSONEncodable] | BaseModel | List[BaseModel] | Dict[JSONEncodable, JSONEncodable] | None


class Request(BaseModel):
    url: StrictStr
    auth: Tuple[StrictStr, StrictStr] | None = None
    headers: Headers | None = None
    params: Params | None = None


class RequestWithData(BaseModel):
    url: StrictStr
    auth: Tuple[StrictStr, StrictStr] | None = None
    headers: Headers | None = None
    params: Params | None = None
    data: Data
    files: list[File | str] | None = None

    class Config:
        arbitrary_types_allowed=True

