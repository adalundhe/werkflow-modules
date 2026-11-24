from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RDSSwitchoverBlueGreenDeploymentRequest(BaseModel):
    BlueGreenDeploymentIdentifier: StrictStr
    SwitchoverTimeout: StrictInt | None = None
