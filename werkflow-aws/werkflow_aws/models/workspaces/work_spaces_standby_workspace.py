from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_tag import WorkSpacesTag


class WorkSpacesStandbyWorkspace(BaseModel):
    PrimaryWorkspaceId: StrictStr | None = None
    VolumeEncryptionKey: StrictStr | None = None
    DirectoryId: StrictStr | None = None
    Tags: list[WorkSpacesTag] | None = None
    DataReplication: StrictStr | None = None
