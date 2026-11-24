from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayGetModelsRequest(BaseModel):
    restApiId: StrictStr
    position: StrictStr | None = None
    limit: StrictInt | None = None
