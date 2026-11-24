from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneDomainMembership(BaseModel):
    Domain: StrictStr | None = None
    Status: StrictStr | None = None
    FQDN: StrictStr | None = None
    IAMRoleName: StrictStr | None = None
