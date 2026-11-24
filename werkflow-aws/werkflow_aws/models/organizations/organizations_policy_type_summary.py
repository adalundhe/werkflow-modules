from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsPolicyTypeSummary(BaseModel):
    Type: StrictStr | None = None
    Status: StrictStr | None = None
