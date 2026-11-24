from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetRoutesRequest(BaseModel):
    ApiId: StrictStr
    MaxResults: StrictStr | None = None
    NextToken: StrictStr | None = None
