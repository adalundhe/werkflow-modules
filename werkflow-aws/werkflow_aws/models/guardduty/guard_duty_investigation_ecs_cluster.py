from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyInvestigationEcsCluster(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Status: StrictStr | None = None
