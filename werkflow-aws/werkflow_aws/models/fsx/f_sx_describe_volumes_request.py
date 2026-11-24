from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_volume_filter import FSxVolumeFilter


class FSxDescribeVolumesRequest(BaseModel):
    VolumeIds: list[StrictStr] | None = None
    Filters: list[FSxVolumeFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
