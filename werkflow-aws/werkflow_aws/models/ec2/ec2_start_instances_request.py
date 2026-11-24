from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2StartInstancesRequest(BaseModel):
    InstanceIds: list[StrictStr]
    AdditionalInfo: StrictStr | None = None
    DryRun: StrictBool | None = None
