from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieAutomatedDiscoveryAccountUpdateError(BaseModel):
    accountId: StrictStr | None = None
    errorCode: StrictStr | None = None
