from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SecurityHubEnableOrganizationAdminAccountRequest(BaseModel):
    AdminAccountId: StrictStr
    Feature: Literal['SecurityHub', 'SecurityHubV2'] | None = None
