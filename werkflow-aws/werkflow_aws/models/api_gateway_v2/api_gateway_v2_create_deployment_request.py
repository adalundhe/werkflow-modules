from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2CreateDeploymentRequest(BaseModel):
    ApiId: StrictStr
    Description: StrictStr | None = None
    StageName: StrictStr | None = None
