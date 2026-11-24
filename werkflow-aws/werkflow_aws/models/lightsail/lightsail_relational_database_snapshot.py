from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_tag import LightsailTag


class LightsailRelationalDatabaseSnapshot(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    supportCode: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    engine: StrictStr | None = None
    engineVersion: StrictStr | None = None
    sizeInGb: StrictInt | None = None
    state: StrictStr | None = None
    fromRelationalDatabaseName: StrictStr | None = None
    fromRelationalDatabaseArn: StrictStr | None = None
    fromRelationalDatabaseBundleId: StrictStr | None = None
    fromRelationalDatabaseBlueprintId: StrictStr | None = None
