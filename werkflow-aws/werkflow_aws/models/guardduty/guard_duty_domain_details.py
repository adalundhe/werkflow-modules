from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyDomainDetails(BaseModel):
    Domain: StrictStr | None = None
