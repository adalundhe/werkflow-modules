from typing import Dict, Optional, Union
from pydantic import BaseModel, StrictStr, Json


Headers = Dict[str, Union[int, float, str, bytes, None]]
Params = Dict[str, str]
Data = Union[str, bytes, BaseModel, None]


class Request(BaseModel):
    url: StrictStr
    headers: Optional[Headers]
    params: Optional[Params]


class RequestWithData(BaseModel):
    url: StrictStr
    headers: Optional[Headers]
    params: Optional[Params]
    data: Data

    class Config:
        arbitrary_types_allowed=True

