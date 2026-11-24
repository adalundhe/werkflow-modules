from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetModelTemplateRequest(BaseModel):
    restApiId: StrictStr
    modelName: StrictStr
