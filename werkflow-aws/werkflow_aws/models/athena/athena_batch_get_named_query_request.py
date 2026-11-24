from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaBatchGetNamedQueryRequest(BaseModel):
    NamedQueryIds: list[StrictStr]
