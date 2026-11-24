from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeleteDeploymentRequest(BaseModel):
    ApiId: StrictStr
    DeploymentId: StrictStr
