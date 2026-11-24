from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMPutAccountPropertiesRequest(BaseModel):
    Properties: dict[StrictStr, StrictStr]
