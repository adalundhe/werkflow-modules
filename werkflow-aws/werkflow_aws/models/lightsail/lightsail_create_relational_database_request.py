from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateRelationalDatabaseRequest(BaseModel):
    relationalDatabaseName: StrictStr
    relationalDatabaseBlueprintId: StrictStr
    relationalDatabaseBundleId: StrictStr
    masterDatabaseName: StrictStr
    masterUsername: StrictStr
    availabilityZone: StrictStr | None = None
    masterUserPassword: StrictStr | None = None
    preferredBackupWindow: StrictStr | None = None
    preferredMaintenanceWindow: StrictStr | None = None
    publiclyAccessible: StrictBool | None = None
    tags: list[LightsailTag] | None = None
