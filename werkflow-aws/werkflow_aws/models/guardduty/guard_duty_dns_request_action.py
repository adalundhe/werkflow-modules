from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GuardDutyDnsRequestAction(BaseModel):
    Domain: StrictStr | None = None
    Protocol: StrictStr | None = None
    Blocked: StrictBool | None = None
    DomainWithSuffix: StrictStr | None = None
    VpcOwnerAccountId: StrictStr | None = None
