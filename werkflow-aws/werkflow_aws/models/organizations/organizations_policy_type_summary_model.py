from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsPolicyTypeSummaryModel(BaseModel):
    Type: StrictStr | None = None
    Status: StrictStr | None = None
