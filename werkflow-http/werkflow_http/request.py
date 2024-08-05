from typing import Dict, Tuple, Union

from pydantic import BaseModel, StrictStr

Headers = Dict[str, Union[int, float, str, bytes, None]]
Params = Dict[str, str]
Data = Union[str, bytes, BaseModel, None]


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

    class Config:
        arbitrary_types_allowed=True

