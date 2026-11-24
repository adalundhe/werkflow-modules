from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayGatewayResponse(BaseModel):
    responseType: StrictStr | None = None
    statusCode: StrictStr | None = None
    responseParameters: dict[StrictStr, StrictStr] | None = None
    responseTemplates: dict[StrictStr, StrictStr] | None = None
    defaultResponse: StrictBool | None = None
