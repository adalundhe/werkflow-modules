from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetAuthorizersRequest(BaseModel):
    ApiId: StrictStr
    MaxResults: StrictStr | None = None
    NextToken: StrictStr | None = None
