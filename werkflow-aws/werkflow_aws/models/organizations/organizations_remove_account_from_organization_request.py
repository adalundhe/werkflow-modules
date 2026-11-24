from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsRemoveAccountFromOrganizationRequest(BaseModel):
    AccountId: StrictStr
