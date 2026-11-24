from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .lightsail_disk import LightsailDisk
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_tag import LightsailTag


class LightsailInstanceSnapshot(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    supportCode: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    state: StrictStr | None = None
    progress: StrictStr | None = None
    fromAttachedDisks: list[LightsailDisk] | None = None
    fromInstanceName: StrictStr | None = None
    fromInstanceArn: StrictStr | None = None
    fromBlueprintId: StrictStr | None = None
    fromBundleId: StrictStr | None = None
    isFromAutoSnapshot: StrictBool | None = None
    sizeInGb: StrictInt | None = None
