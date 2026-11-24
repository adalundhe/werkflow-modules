from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2EnableApplicationStatusCheckSuppressionRequest(BaseModel):
    InstanceIds: list[StrictStr] | None = None
    DurationSeconds: StrictInt | None = None
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
