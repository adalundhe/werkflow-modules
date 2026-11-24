from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .work_spaces_tag import WorkSpacesTag
from .work_spaces_workspace_properties import WorkSpacesWorkspaceProperties


class WorkSpacesWorkspaceRequest(BaseModel):
    DirectoryId: StrictStr | None = None
    UserName: StrictStr | None = None
    BundleId: StrictStr | None = None
    VolumeEncryptionKey: StrictStr | None = None
    UserVolumeEncryptionEnabled: StrictBool | None = None
    RootVolumeEncryptionEnabled: StrictBool | None = None
    WorkspaceProperties: WorkSpacesWorkspaceProperties | None = None
    Tags: list[WorkSpacesTag] | None = None
    WorkspaceName: StrictStr | None = None
    Ipv6Address: StrictStr | None = None
