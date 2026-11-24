from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class MacieAutomatedDiscoveryAccountUpdate(BaseModel):
    accountId: StrictStr | None = None
    status: Literal['ENABLED', 'DISABLED'] | None = None
