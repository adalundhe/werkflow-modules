from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_admin_account import MacieAdminAccount


class MacieListOrganizationAdminAccountsResponse(BaseModel):
    adminAccounts: list[MacieAdminAccount] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
