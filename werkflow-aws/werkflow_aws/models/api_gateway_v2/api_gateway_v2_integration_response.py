from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2IntegrationResponse(BaseModel):
    ContentHandlingStrategy: StrictStr | None = None
    IntegrationResponseId: StrictStr | None = None
    IntegrationResponseKey: StrictStr | None = None
    ResponseParameters: dict[StrictStr, StrictStr] | None = None
    ResponseTemplates: dict[StrictStr, StrictStr] | None = None
    TemplateSelectionExpression: StrictStr | None = None
