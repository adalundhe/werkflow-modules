from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QBusinessMemberUser(BaseModel):
    userId: StrictStr
    type: Literal['INDEX', 'DATASOURCE'] | None = None
