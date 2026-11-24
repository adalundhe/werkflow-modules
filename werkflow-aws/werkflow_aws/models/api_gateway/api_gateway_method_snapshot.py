from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayMethodSnapshot(BaseModel):
    authorizationType: StrictStr | None = None
    apiKeyRequired: StrictBool | None = None
