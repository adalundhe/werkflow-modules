from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyResourceDetails(BaseModel):
    InstanceArn: StrictStr | None = None
