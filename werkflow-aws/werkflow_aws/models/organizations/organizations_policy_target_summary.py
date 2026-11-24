from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsPolicyTargetSummary(BaseModel):
    TargetId: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
