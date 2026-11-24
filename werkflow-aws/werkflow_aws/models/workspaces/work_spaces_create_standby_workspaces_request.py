from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_standby_workspace import WorkSpacesStandbyWorkspace


class WorkSpacesCreateStandbyWorkspacesRequest(BaseModel):
    PrimaryRegion: StrictStr
    StandbyWorkspaces: list[WorkSpacesStandbyWorkspace]
