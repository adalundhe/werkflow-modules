from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_volume_recycle_bin_info import EC2VolumeRecycleBinInfo


class EC2ListVolumesInRecycleBinResponse(BaseModel):
    Volumes: list[EC2VolumeRecycleBinInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
