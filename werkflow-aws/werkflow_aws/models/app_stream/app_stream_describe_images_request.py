from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class AppStreamDescribeImagesRequest(BaseModel):
    Names: list[StrictStr] | None = None
    Arns: list[StrictStr] | None = None
    Type: Literal['PUBLIC', 'PRIVATE', 'SHARED'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
