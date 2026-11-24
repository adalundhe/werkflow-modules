from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_disk_image_description import EC2DiskImageDescription
from .ec2_disk_image_volume_description import EC2DiskImageVolumeDescription


class EC2ImportVolumeTaskDetails(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    BytesConverted: StrictInt | None = None
    Description: StrictStr | None = None
    Image: EC2DiskImageDescription | None = None
    Volume: EC2DiskImageVolumeDescription | None = None
