from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesMigrateWorkspaceRequest(BaseModel):
    SourceWorkspaceId: StrictStr
    BundleId: StrictStr
