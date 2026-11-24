from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesAssociateWorkspaceApplicationRequest(BaseModel):
    WorkspaceId: StrictStr
    ApplicationId: StrictStr
