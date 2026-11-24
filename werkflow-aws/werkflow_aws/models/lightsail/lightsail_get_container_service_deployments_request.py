from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetContainerServiceDeploymentsRequest(BaseModel):
    serviceName: StrictStr
