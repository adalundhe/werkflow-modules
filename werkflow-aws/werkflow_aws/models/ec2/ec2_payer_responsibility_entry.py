from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PayerResponsibilityEntry(BaseModel):
    Scope: StrictStr | None = None
    PayerResponsibilityType: StrictStr | None = None
