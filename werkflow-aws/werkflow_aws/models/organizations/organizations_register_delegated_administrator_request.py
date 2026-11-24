from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsRegisterDelegatedAdministratorRequest(BaseModel):
    AccountId: StrictStr
    ServicePrincipal: StrictStr
