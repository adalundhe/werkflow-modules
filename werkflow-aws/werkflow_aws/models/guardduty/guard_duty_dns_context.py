from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDnsContext(BaseModel):
    DomainSuffix: StrictStr | None = None
    OtherDomains: StrictStr | None = None
    ResolverHistory: StrictStr | None = None
