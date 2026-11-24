from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesStopWorkspacesPoolRequest(BaseModel):
    PoolId: StrictStr
