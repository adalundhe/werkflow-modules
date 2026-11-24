from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_disk_image_detail import EC2DiskImageDetail
from .ec2_volume_detail import EC2VolumeDetail


class EC2DiskImage(BaseModel):
    Description: StrictStr | None = None
    Image: EC2DiskImageDetail | None = None
    Volume: EC2VolumeDetail | None = None
