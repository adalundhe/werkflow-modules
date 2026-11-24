from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QBusinessPrincipalGroup(BaseModel):
    access: Literal['ALLOW', 'DENY']
    name: StrictStr | None = None
    membershipType: Literal['INDEX', 'DATASOURCE'] | None = None
