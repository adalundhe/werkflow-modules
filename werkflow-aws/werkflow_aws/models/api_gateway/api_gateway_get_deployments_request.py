from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayGetDeploymentsRequest(BaseModel):
    restApiId: StrictStr
    position: StrictStr | None = None
    limit: StrictInt | None = None
