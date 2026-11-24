from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .work_spaces_thin_client_maintenance_window import WorkSpacesThinClientMaintenanceWindow


class WorkSpacesThinClientUpdateEnvironmentRequest(BaseModel):
    id: StrictStr
    name: StrictStr | None = None
    desktopArn: StrictStr | None = None
    desktopEndpoint: StrictStr | None = None
    softwareSetUpdateSchedule: Literal['USE_MAINTENANCE_WINDOW', 'APPLY_IMMEDIATELY'] | None = None
    maintenanceWindow: WorkSpacesThinClientMaintenanceWindow | None = None
    softwareSetUpdateMode: Literal['USE_LATEST', 'USE_DESIRED'] | None = None
    desiredSoftwareSetId: StrictStr | None = None
    deviceCreationTags: dict[StrictStr, StrictStr] | None = None
