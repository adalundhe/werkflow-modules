from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2UpdateDeploymentRequest(BaseModel):
    ApiId: StrictStr
    DeploymentId: StrictStr
    Description: StrictStr | None = None
