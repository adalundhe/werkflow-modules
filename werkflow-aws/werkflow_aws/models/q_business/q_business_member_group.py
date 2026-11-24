from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QBusinessMemberGroup(BaseModel):
    groupName: StrictStr
    type: Literal['INDEX', 'DATASOURCE'] | None = None
