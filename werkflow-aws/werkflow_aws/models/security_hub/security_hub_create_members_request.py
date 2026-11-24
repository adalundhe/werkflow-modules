from __future__ import annotations
from pydantic import BaseModel
from .security_hub_account_details import SecurityHubAccountDetails


class SecurityHubCreateMembersRequest(BaseModel):
    AccountDetails: list[SecurityHubAccountDetails]
