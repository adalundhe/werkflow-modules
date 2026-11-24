from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchUpdateServiceAccessPoliciesRequest(BaseModel):
    DomainName: StrictStr
    AccessPolicies: StrictStr
