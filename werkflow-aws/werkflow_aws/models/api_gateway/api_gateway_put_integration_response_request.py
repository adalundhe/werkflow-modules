from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class APIGatewayPutIntegrationResponseRequest(BaseModel):
    restApiId: StrictStr
    resourceId: StrictStr
    httpMethod: StrictStr
    statusCode: StrictStr
    selectionPattern: StrictStr | None = None
    responseParameters: dict[StrictStr, StrictStr] | None = None
    responseTemplates: dict[StrictStr, StrictStr] | None = None
    contentHandling: Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT'] | None = None
