from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class APIGatewayPutIntegrationResponseResponse(BaseModel):
    statusCode: StrictStr | None = None
    selectionPattern: StrictStr | None = None
    responseParameters: dict[StrictStr, StrictStr] | None = None
    responseTemplates: dict[StrictStr, StrictStr] | None = None
    contentHandling: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
