from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_work_space_application_deployment import WorkSpacesWorkSpaceApplicationDeployment


class WorkSpacesDeployWorkspaceApplicationsResponse(BaseModel):
    Deployment: WorkSpacesWorkSpaceApplicationDeployment | None = None
    ResponseMetadata: dict[str, Any] | None = None
