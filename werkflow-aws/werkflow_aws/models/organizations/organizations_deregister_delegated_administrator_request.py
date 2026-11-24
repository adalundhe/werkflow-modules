from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsDeregisterDelegatedAdministratorRequest(BaseModel):
    AccountId: StrictStr
    ServicePrincipal: StrictStr
