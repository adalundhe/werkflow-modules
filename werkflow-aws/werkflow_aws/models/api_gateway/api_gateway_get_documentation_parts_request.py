from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayGetDocumentationPartsRequest(BaseModel):
    restApiId: StrictStr
    type: Literal['API', 'AUTHORIZER', 'MODEL', 'RESOURCE', 'METHOD', 'PATH_PARAMETER', 'QUERY_PARAMETER', 'REQUEST_HEADER', 'REQUEST_BODY', 'RESPONSE', 'RESPONSE_HEADER', 'RESPONSE_BODY'] | None = None
    nameQuery: StrictStr | None = None
    path: StrictStr | None = None
    position: StrictStr | None = None
    limit: StrictInt | None = None
    locationStatus: Literal['DOCUMENTED', 'UNDOCUMENTED'] | None = None
