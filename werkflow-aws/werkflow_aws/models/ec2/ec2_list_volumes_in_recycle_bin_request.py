from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ListVolumesInRecycleBinRequest(BaseModel):
    VolumeIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
