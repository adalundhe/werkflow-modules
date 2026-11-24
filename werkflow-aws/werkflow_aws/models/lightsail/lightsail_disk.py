from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .lightsail_add_on import LightsailAddOn
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_tag import LightsailTag


class LightsailDisk(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    supportCode: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    addOns: list[LightsailAddOn] | None = None
    sizeInGb: StrictInt | None = None
    isSystemDisk: StrictBool | None = None
    iops: StrictInt | None = None
    path: StrictStr | None = None
    state: StrictStr | None = None
    attachedTo: StrictStr | None = None
    isAttached: StrictBool | None = None
    attachmentState: StrictStr | None = None
    gbInUse: StrictInt | None = None
    autoMountStatus: StrictStr | None = None
