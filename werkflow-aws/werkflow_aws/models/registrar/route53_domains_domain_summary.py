from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class Route53DomainsDomainSummary(BaseModel):
    DomainName: StrictStr | None = None
    AutoRenew: StrictBool | None = None
    TransferLock: StrictBool | None = None
    Expiry: datetime.datetime | StrictStr | None = None
