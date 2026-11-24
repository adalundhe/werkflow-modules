from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .organizations_account_model import OrganizationsAccountModel


class OrganizationsListAccountsWithInvalidEffectivePolicyResponse(BaseModel):
    Accounts: list[OrganizationsAccountModel] | None = None
    PolicyType: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
