from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetStagesRequest(BaseModel):
    restApiId: StrictStr
    deploymentId: StrictStr | None = None
