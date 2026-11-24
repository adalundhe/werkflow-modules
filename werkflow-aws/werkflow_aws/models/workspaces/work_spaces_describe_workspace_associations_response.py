from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_workspace_resource_association import WorkSpacesWorkspaceResourceAssociation


class WorkSpacesDescribeWorkspaceAssociationsResponse(BaseModel):
    Associations: list[WorkSpacesWorkspaceResourceAssociation] | None = None
    ResponseMetadata: dict[str, Any] | None = None
