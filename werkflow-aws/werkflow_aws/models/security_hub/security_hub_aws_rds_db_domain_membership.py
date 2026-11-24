from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRdsDbDomainMembership(BaseModel):
    Domain: StrictStr | None = None
    Status: StrictStr | None = None
    Fqdn: StrictStr | None = None
    IamRoleName: StrictStr | None = None
