from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .work_spaces_application_settings_request import WorkSpacesApplicationSettingsRequest
from .work_spaces_capacity import WorkSpacesCapacity
from .work_spaces_timeout_settings import WorkSpacesTimeoutSettings


class WorkSpacesUpdateWorkspacesPoolRequest(BaseModel):
    PoolId: StrictStr
    Description: StrictStr | None = None
    BundleId: StrictStr | None = None
    DirectoryId: StrictStr | None = None
    Capacity: WorkSpacesCapacity | None = None
    ApplicationSettings: WorkSpacesApplicationSettingsRequest | None = None
    TimeoutSettings: WorkSpacesTimeoutSettings | None = None
    RunningMode: Literal['AUTO_STOP', 'ALWAYS_ON'] | None = None
