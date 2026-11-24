from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSDeleteBlueGreenDeploymentRequest(BaseModel):
    BlueGreenDeploymentIdentifier: StrictStr
    DeleteTarget: StrictBool | None = None
