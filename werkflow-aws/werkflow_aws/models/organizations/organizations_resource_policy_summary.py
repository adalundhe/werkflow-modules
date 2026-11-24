from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsResourcePolicySummary(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
