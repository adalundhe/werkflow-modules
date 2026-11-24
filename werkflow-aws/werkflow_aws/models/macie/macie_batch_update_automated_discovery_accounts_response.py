from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .macie_automated_discovery_account_update_error import MacieAutomatedDiscoveryAccountUpdateError


class MacieBatchUpdateAutomatedDiscoveryAccountsResponse(BaseModel):
    errors: list[MacieAutomatedDiscoveryAccountUpdateError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
