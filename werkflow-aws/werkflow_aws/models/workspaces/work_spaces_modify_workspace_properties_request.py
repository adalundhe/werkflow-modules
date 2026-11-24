from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .work_spaces_workspace_properties import WorkSpacesWorkspaceProperties


class WorkSpacesModifyWorkspacePropertiesRequest(BaseModel):
    WorkspaceId: StrictStr
    WorkspaceProperties: WorkSpacesWorkspaceProperties | None = None
    DataReplication: Literal['NO_REPLICATION', 'PRIMARY_AS_SOURCE'] | None = None
