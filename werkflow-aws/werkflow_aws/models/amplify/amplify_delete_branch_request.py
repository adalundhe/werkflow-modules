from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyDeleteBranchRequest(BaseModel):
    appId: StrictStr
    branchName: StrictStr
