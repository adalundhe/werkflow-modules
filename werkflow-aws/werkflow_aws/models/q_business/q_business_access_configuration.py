from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .q_business_access_control import QBusinessAccessControl


class QBusinessAccessConfiguration(BaseModel):
    accessControls: list[QBusinessAccessControl]
    memberRelation: Literal['AND', 'OR'] | None = None
