from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2EbsInstanceBlockDeviceSpecification(BaseModel):
    VolumeId: StrictStr | None = None
    DeleteOnTermination: StrictBool | None = None
