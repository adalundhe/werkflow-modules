from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_volume_status_details import EC2VolumeStatusDetails


class EC2VolumeStatusInfo(BaseModel):
    Details: list[EC2VolumeStatusDetails] | None = None
    Status: StrictStr | None = None
