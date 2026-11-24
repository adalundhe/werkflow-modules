from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayIntegrationResponse(BaseModel):
    statusCode: StrictStr | None = None
    selectionPattern: StrictStr | None = None
    responseParameters: dict[StrictStr, StrictStr] | None = None
    responseTemplates: dict[StrictStr, StrictStr] | None = None
    contentHandling: StrictStr | None = None
