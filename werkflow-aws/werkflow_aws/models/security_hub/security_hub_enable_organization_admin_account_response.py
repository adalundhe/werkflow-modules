from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SecurityHubEnableOrganizationAdminAccountResponse(BaseModel):
    AdminAccountId: StrictStr | None = None
    Feature: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
