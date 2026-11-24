from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsEnableAWSServiceAccessRequest(BaseModel):
    ServicePrincipal: StrictStr
