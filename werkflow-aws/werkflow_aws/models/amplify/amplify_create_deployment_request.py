from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyCreateDeploymentRequest(BaseModel):
    appId: StrictStr
    branchName: StrictStr
    fileMap: dict[StrictStr, StrictStr] | None = None
