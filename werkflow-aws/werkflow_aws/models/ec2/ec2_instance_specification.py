from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2InstanceSpecification(BaseModel):
    InstanceId: StrictStr
    ExcludeBootVolume: StrictBool | None = None
    ExcludeDataVolumeIds: list[StrictStr] | None = None
