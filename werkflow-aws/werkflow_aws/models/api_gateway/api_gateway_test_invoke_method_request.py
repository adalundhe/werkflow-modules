from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayTestInvokeMethodRequest(BaseModel):
    restApiId: StrictStr
    resourceId: StrictStr
    httpMethod: StrictStr
    pathWithQueryString: StrictStr | None = None
    body: StrictStr | None = None
    headers: dict[StrictStr, StrictStr] | None = None
    multiValueHeaders: dict[StrictStr, list[StrictStr]] | None = None
    clientCertificateId: StrictStr | None = None
    stageVariables: dict[StrictStr, StrictStr] | None = None
