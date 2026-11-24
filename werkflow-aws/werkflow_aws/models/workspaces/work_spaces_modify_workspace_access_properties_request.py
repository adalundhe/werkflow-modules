from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_workspace_access_properties import WorkSpacesWorkspaceAccessProperties


class WorkSpacesModifyWorkspaceAccessPropertiesRequest(BaseModel):
    ResourceId: StrictStr
    WorkspaceAccessProperties: WorkSpacesWorkspaceAccessProperties
