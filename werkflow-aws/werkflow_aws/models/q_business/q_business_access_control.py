from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .q_business_principal import QBusinessPrincipal


class QBusinessAccessControl(BaseModel):
    principals: list[QBusinessPrincipal]
    memberRelation: Literal['AND', 'OR'] | None = None
