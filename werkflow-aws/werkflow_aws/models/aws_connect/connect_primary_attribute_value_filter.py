from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPrimaryAttributeValueFilter(BaseModel):
    AttributeName: StrictStr
    Values: list[StrictStr]
