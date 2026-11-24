from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesDisassociateWorkspaceApplicationRequest(BaseModel):
    WorkspaceId: StrictStr
    ApplicationId: StrictStr
