from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .work_spaces_application_settings_response import WorkSpacesApplicationSettingsResponse
from .work_spaces_capacity_status import WorkSpacesCapacityStatus
from .work_spaces_timeout_settings import WorkSpacesTimeoutSettings
from .workspaces_pool_error import WorkspacesPoolError


class WorkspacesPool(BaseModel):
    PoolId: StrictStr | None = None
    PoolArn: StrictStr | None = None
    CapacityStatus: WorkSpacesCapacityStatus | None = None
    PoolName: StrictStr | None = None
    Description: StrictStr | None = None
    State: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    BundleId: StrictStr | None = None
    DirectoryId: StrictStr | None = None
    Errors: list[WorkspacesPoolError] | None = None
    ApplicationSettings: WorkSpacesApplicationSettingsResponse | None = None
    TimeoutSettings: WorkSpacesTimeoutSettings | None = None
    RunningMode: StrictStr | None = None
