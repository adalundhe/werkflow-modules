from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetSdkRequest(BaseModel):
    restApiId: StrictStr
    stageName: StrictStr
    sdkType: StrictStr
    parameters: dict[StrictStr, StrictStr] | None = None
