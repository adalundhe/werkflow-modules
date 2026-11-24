from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class APIGatewayV2UpdateIntegrationResponseRequest(BaseModel):
    ApiId: StrictStr
    IntegrationId: StrictStr
    IntegrationResponseId: StrictStr
    ContentHandlingStrategy: Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT'] | None = None
    IntegrationResponseKey: StrictStr | None = None
    ResponseParameters: dict[StrictStr, StrictStr] | None = None
    ResponseTemplates: dict[StrictStr, StrictStr] | None = None
    TemplateSelectionExpression: StrictStr | None = None
