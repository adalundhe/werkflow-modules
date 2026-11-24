from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyGetBranchRequest(BaseModel):
    appId: StrictStr
    branchName: StrictStr
