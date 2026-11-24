from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_image_watermark import EC2ImageWatermark


class EC2ImageMetadata(BaseModel):
    ImageId: StrictStr | None = None
    Name: StrictStr | None = None
    OwnerId: StrictStr | None = None
    State: StrictStr | None = None
    ImageOwnerAlias: StrictStr | None = None
    CreationDate: StrictStr | None = None
    DeprecationTime: StrictStr | None = None
    ImageAllowed: StrictBool | None = None
    IsPublic: StrictBool | None = None
    ImageWatermarks: list[EC2ImageWatermark] | None = None
