from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyInvestigationEksCluster(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Status: StrictStr | None = None
    VpcId: StrictStr | None = None
