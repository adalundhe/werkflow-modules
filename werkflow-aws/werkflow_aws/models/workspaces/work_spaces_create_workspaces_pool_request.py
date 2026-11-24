from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .work_spaces_application_settings_request import WorkSpacesApplicationSettingsRequest
from .work_spaces_capacity import WorkSpacesCapacity
from .work_spaces_tag import WorkSpacesTag
from .work_spaces_timeout_settings import WorkSpacesTimeoutSettings


class WorkSpacesCreateWorkspacesPoolRequest(BaseModel):
    PoolName: StrictStr
    Description: StrictStr
    BundleId: StrictStr
    DirectoryId: StrictStr
    Capacity: WorkSpacesCapacity
    Tags: list[WorkSpacesTag] | None = None
    ApplicationSettings: WorkSpacesApplicationSettingsRequest | None = None
    TimeoutSettings: WorkSpacesTimeoutSettings | None = None
    RunningMode: Literal['AUTO_STOP', 'ALWAYS_ON'] | None = None
