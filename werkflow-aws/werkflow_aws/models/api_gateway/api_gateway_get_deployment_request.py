from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetDeploymentRequest(BaseModel):
    restApiId: StrictStr
    deploymentId: StrictStr
    embed: list[StrictStr] | None = None
