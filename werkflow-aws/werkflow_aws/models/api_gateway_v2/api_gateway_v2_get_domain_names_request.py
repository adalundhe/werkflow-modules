from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetDomainNamesRequest(BaseModel):
    MaxResults: StrictStr | None = None
    NextToken: StrictStr | None = None
