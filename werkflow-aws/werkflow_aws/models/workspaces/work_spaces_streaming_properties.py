from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_global_accelerator_for_directory import WorkSpacesGlobalAcceleratorForDirectory
from .work_spaces_storage_connector import WorkSpacesStorageConnector
from .work_spaces_user_setting import WorkSpacesUserSetting


class WorkSpacesStreamingProperties(BaseModel):
    StreamingExperiencePreferredProtocol: StrictStr | None = None
    UserSettings: list[WorkSpacesUserSetting] | None = None
    StorageConnectors: list[WorkSpacesStorageConnector] | None = None
    GlobalAccelerator: WorkSpacesGlobalAcceleratorForDirectory | None = None
