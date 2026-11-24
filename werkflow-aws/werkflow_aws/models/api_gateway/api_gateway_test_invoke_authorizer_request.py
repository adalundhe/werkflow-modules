from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayTestInvokeAuthorizerRequest(BaseModel):
    restApiId: StrictStr
    authorizerId: StrictStr
    headers: dict[StrictStr, StrictStr] | None = None
    multiValueHeaders: dict[StrictStr, list[StrictStr]] | None = None
    pathWithQueryString: StrictStr | None = None
    body: StrictStr | None = None
    stageVariables: dict[StrictStr, StrictStr] | None = None
    additionalContext: dict[StrictStr, StrictStr] | None = None
