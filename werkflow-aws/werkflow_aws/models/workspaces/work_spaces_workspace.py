from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .work_spaces_data_replication_settings import WorkSpacesDataReplicationSettings
from .work_spaces_modification_state import WorkSpacesModificationState
from .work_spaces_related_workspace_properties import WorkSpacesRelatedWorkspaceProperties
from .work_spaces_standby_workspaces_properties import WorkSpacesStandbyWorkspacesProperties
from .work_spaces_workspace_properties import WorkSpacesWorkspaceProperties


class WorkSpacesWorkspace(BaseModel):
    WorkspaceId: StrictStr | None = None
    DirectoryId: StrictStr | None = None
    UserName: StrictStr | None = None
    IpAddress: StrictStr | None = None
    Ipv6Address: StrictStr | None = None
    State: StrictStr | None = None
    BundleId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    ComputerName: StrictStr | None = None
    VolumeEncryptionKey: StrictStr | None = None
    UserVolumeEncryptionEnabled: StrictBool | None = None
    RootVolumeEncryptionEnabled: StrictBool | None = None
    WorkspaceName: StrictStr | None = None
    WorkspaceProperties: WorkSpacesWorkspaceProperties | None = None
    ModificationStates: list[WorkSpacesModificationState] | None = None
    RelatedWorkspaces: list[WorkSpacesRelatedWorkspaceProperties] | None = None
    DataReplicationSettings: WorkSpacesDataReplicationSettings | None = None
    StandbyWorkspacesProperties: list[WorkSpacesStandbyWorkspacesProperties] | None = None
