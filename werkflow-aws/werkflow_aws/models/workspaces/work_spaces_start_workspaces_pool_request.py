from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesStartWorkspacesPoolRequest(BaseModel):
    PoolId: StrictStr
