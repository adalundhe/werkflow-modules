from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailQueryStringObject(BaseModel):
    option: StrictBool | None = None
    queryStringsAllowList: list[StrictStr] | None = None
