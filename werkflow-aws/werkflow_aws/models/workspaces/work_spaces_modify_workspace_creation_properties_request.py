from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_workspace_creation_properties import WorkSpacesWorkspaceCreationProperties


class WorkSpacesModifyWorkspaceCreationPropertiesRequest(BaseModel):
    ResourceId: StrictStr
    WorkspaceCreationProperties: WorkSpacesWorkspaceCreationProperties
