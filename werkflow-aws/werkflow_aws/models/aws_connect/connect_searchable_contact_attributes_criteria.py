from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectSearchableContactAttributesCriteria(BaseModel):
    Key: StrictStr
    Values: list[StrictStr]
