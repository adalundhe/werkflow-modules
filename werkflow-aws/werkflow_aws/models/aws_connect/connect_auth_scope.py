from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectAuthScope(BaseModel):
    EntityType: Literal['CUSTOMER_PROFILE']
    SecurityProfileIds: list[StrictStr] | None = None
    EntityId: StrictStr | None = None
    DomainName: StrictStr | None = None
