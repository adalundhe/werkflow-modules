from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class StorageGatewayDetachVolumeRequest(BaseModel):
    VolumeARN: StrictStr
    ForceDetach: StrictBool | None = None
