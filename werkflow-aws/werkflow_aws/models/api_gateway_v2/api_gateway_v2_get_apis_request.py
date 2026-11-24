from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetApisRequest(BaseModel):
    MaxResults: StrictStr | None = None
    NextToken: StrictStr | None = None
