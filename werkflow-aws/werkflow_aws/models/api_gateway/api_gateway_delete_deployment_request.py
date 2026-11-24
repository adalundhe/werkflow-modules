from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteDeploymentRequest(BaseModel):
    restApiId: StrictStr
    deploymentId: StrictStr
