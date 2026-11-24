from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .lightsail_pending_maintenance_action import LightsailPendingMaintenanceAction
from .lightsail_pending_modified_relational_database_values import LightsailPendingModifiedRelationalDatabaseValues
from .lightsail_relational_database_endpoint import LightsailRelationalDatabaseEndpoint
from .lightsail_relational_database_hardware import LightsailRelationalDatabaseHardware
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_tag import LightsailTag


class LightsailRelationalDatabase(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    supportCode: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    tags: list[LightsailTag] | None = None
    relationalDatabaseBlueprintId: StrictStr | None = None
    relationalDatabaseBundleId: StrictStr | None = None
    masterDatabaseName: StrictStr | None = None
    hardware: LightsailRelationalDatabaseHardware | None = None
    state: StrictStr | None = None
    secondaryAvailabilityZone: StrictStr | None = None
    backupRetentionEnabled: StrictBool | None = None
    pendingModifiedValues: LightsailPendingModifiedRelationalDatabaseValues | None = None
    engine: StrictStr | None = None
    engineVersion: StrictStr | None = None
    latestRestorableTime: datetime.datetime | StrictStr | None = None
    masterUsername: StrictStr | None = None
    parameterApplyStatus: StrictStr | None = None
    preferredBackupWindow: StrictStr | None = None
    preferredMaintenanceWindow: StrictStr | None = None
    publiclyAccessible: StrictBool | None = None
    masterEndpoint: LightsailRelationalDatabaseEndpoint | None = None
    pendingMaintenanceActions: list[LightsailPendingMaintenanceAction] | None = None
    caCertificateIdentifier: StrictStr | None = None
