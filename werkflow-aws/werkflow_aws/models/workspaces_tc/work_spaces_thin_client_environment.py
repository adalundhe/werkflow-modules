from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .work_spaces_thin_client_maintenance_window import WorkSpacesThinClientMaintenanceWindow


class WorkSpacesThinClientEnvironment(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    desktopArn: StrictStr | None = None
    desktopEndpoint: StrictStr | None = None
    desktopType: StrictStr | None = None
    activationCode: StrictStr | None = None
    registeredDevicesCount: StrictInt | None = None
    softwareSetUpdateSchedule: StrictStr | None = None
    maintenanceWindow: WorkSpacesThinClientMaintenanceWindow | None = None
    softwareSetUpdateMode: StrictStr | None = None
    desiredSoftwareSetId: StrictStr | None = None
    pendingSoftwareSetId: StrictStr | None = None
    pendingSoftwareSetVersion: StrictStr | None = None
    softwareSetComplianceStatus: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    arn: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
    deviceCreationTags: dict[StrictStr, StrictStr] | None = None
