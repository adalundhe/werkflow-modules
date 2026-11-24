from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class APIGatewayV2CreateIntegrationResponseRequest(BaseModel):
    ApiId: StrictStr
    IntegrationId: StrictStr
    IntegrationResponseKey: StrictStr
    ContentHandlingStrategy: Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT'] | None = None
    ResponseParameters: dict[StrictStr, StrictStr] | None = None
    ResponseTemplates: dict[StrictStr, StrictStr] | None = None
    TemplateSelectionExpression: StrictStr | None = None
