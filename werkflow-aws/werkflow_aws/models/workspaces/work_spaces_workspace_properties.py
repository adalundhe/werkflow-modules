from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .work_spaces_global_accelerator_for_work_space import WorkSpacesGlobalAcceleratorForWorkSpace


class WorkSpacesWorkspaceProperties(BaseModel):
    RunningMode: StrictStr | None = None
    RunningModeAutoStopTimeoutInMinutes: StrictInt | None = None
    RootVolumeSizeGib: StrictInt | None = None
    UserVolumeSizeGib: StrictInt | None = None
    ComputeTypeName: StrictStr | None = None
    Protocols: list[StrictStr] | None = None
    OperatingSystemName: StrictStr | None = None
    GlobalAccelerator: WorkSpacesGlobalAcceleratorForWorkSpace | None = None
    NestedVirtualizationEnabled: StrictBool | None = None
