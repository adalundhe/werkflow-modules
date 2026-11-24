from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ModifyVolumeRequest(BaseModel):
    VolumeId: StrictStr
    DryRun: StrictBool | None = None
    Size: StrictInt | None = None
    VolumeType: Literal['standard', 'io1', 'io2', 'gp2', 'sc1', 'st1', 'gp3'] | None = None
    Iops: StrictInt | None = None
    Throughput: StrictInt | None = None
    MultiAttachEnabled: StrictBool | None = None
