from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_disk_image_detail import EC2DiskImageDetail
from .ec2_volume_detail import EC2VolumeDetail


class EC2ImportVolumeRequest(BaseModel):
    Image: EC2DiskImageDetail
    Volume: EC2VolumeDetail
    AvailabilityZoneId: StrictStr | None = None
    DryRun: StrictBool | None = None
    AvailabilityZone: StrictStr | None = None
    Description: StrictStr | None = None
