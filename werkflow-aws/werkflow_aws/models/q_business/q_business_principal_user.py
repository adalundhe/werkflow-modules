from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QBusinessPrincipalUser(BaseModel):
    access: Literal['ALLOW', 'DENY']
    id: StrictStr | None = None
    membershipType: Literal['INDEX', 'DATASOURCE'] | None = None
