from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectSearchableSegmentAttributesCriteria(BaseModel):
    Key: StrictStr
    Values: list[StrictStr]
