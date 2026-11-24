from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_admin_account import SecurityHubAdminAccount


class SecurityHubListOrganizationAdminAccountsResponse(BaseModel):
    AdminAccounts: list[SecurityHubAdminAccount] | None = None
    NextToken: StrictStr | None = None
    Feature: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
