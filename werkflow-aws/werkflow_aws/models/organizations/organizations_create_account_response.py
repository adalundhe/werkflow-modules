from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .organizations_create_account_status import OrganizationsCreateAccountStatus


class OrganizationsCreateAccountResponse(BaseModel):
    CreateAccountStatus: OrganizationsCreateAccountStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
