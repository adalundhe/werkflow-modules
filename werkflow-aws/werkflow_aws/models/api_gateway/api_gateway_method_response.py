from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayMethodResponse(BaseModel):
    statusCode: StrictStr | None = None
    responseParameters: dict[StrictStr, StrictBool] | None = None
    responseModels: dict[StrictStr, StrictStr] | None = None
