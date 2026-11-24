from __future__ import annotations
from pydantic import BaseModel
from .macie_automated_discovery_account_update import MacieAutomatedDiscoveryAccountUpdate


class MacieBatchUpdateAutomatedDiscoveryAccountsRequest(BaseModel):
    accounts: list[MacieAutomatedDiscoveryAccountUpdate] | None = None
