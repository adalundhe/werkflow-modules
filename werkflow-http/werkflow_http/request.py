from collections.abc import Mapping
from typing import Any, Dict, List, Tuple, Union

from pydantic import BaseModel, ConfigDict, InstanceOf, StrictStr
from .connections.http.models.http import File as File

Headers = Mapping[str, Union[int, float, str, bytes, None]]
Params = Mapping[str, Union[str, int, float, bool, None]]

JSONEncodable = Union[str, bool, int, float, None]
Data = Union[
    JSONEncodable,
    bytes,
    List[Any],
    Dict[str, Any],
    InstanceOf[BaseModel],
]


class Request(BaseModel):
    url: StrictStr
    auth: Tuple[StrictStr, StrictStr] | None = None
    headers: Headers | None = None
    params: Params | None = None


class RequestWithData(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    url: StrictStr
    auth: Tuple[StrictStr, StrictStr] | None = None
    headers: Headers | None = None
    params: Params | None = None
    data: Data = None
    files: list[File | str] | None = None
