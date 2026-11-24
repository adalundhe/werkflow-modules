from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .guard_duty_admin_account import GuardDutyAdminAccount


class GuardDutyListOrganizationAdminAccountsResponse(BaseModel):
    AdminAccounts: list[GuardDutyAdminAccount] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
