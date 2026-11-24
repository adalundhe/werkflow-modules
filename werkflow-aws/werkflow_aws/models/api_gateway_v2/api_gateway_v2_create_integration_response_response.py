from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class APIGatewayV2CreateIntegrationResponseResponse(BaseModel):
    ContentHandlingStrategy: StrictStr | None = None
    IntegrationResponseId: StrictStr | None = None
    IntegrationResponseKey: StrictStr | None = None
    ResponseParameters: dict[StrictStr, StrictStr] | None = None
    ResponseTemplates: dict[StrictStr, StrictStr] | None = None
    TemplateSelectionExpression: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
