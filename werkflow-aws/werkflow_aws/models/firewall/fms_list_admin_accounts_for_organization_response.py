from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fms_admin_account_summary import FMSAdminAccountSummary


class FMSListAdminAccountsForOrganizationResponse(BaseModel):
    AdminAccounts: list[FMSAdminAccountSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
