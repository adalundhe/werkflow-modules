from __future__ import annotations
from pydantic import BaseModel
from .work_spaces_workspace_resource_association import WorkSpacesWorkspaceResourceAssociation


class WorkSpacesWorkSpaceApplicationDeployment(BaseModel):
    Associations: list[WorkSpacesWorkspaceResourceAssociation] | None = None
