from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .organizations_create_account_status import OrganizationsCreateAccountStatus


class OrganizationsListCreateAccountStatusResponse(BaseModel):
    CreateAccountStatuses: list[OrganizationsCreateAccountStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
