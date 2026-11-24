from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DisableApplicationStatusCheckSuppressionRequest(BaseModel):
    InstanceIds: list[StrictStr] | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
