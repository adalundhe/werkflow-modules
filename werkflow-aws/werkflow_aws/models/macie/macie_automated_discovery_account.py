from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieAutomatedDiscoveryAccount(BaseModel):
    accountId: StrictStr | None = None
    status: StrictStr | None = None
