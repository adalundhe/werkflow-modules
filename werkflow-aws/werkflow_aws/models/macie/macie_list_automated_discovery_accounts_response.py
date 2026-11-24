from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_automated_discovery_account import MacieAutomatedDiscoveryAccount


class MacieListAutomatedDiscoveryAccountsResponse(BaseModel):
    items: list[MacieAutomatedDiscoveryAccount] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
