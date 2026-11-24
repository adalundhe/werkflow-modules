from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .macie_unprocessed_account import MacieUnprocessedAccount


class MacieDeleteInvitationsResponse(BaseModel):
    unprocessedAccounts: list[MacieUnprocessedAccount] | None = None
    ResponseMetadata: dict[str, Any] | None = None
