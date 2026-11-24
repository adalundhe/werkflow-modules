from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayGetSdkTypesRequest(BaseModel):
    position: StrictStr | None = None
    limit: StrictInt | None = None
