from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesSelfservicePermissions(BaseModel):
    RestartWorkspace: StrictStr | None = None
    IncreaseVolumeSize: StrictStr | None = None
    ChangeComputeType: StrictStr | None = None
    SwitchRunningMode: StrictStr | None = None
    RebuildWorkspace: StrictStr | None = None
    NestedVirtualization: StrictStr | None = None
    EnableEndUserAdvisor: StrictStr | None = None
