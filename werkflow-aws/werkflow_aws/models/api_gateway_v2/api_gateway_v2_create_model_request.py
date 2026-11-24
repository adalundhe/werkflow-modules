from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2CreateModelRequest(BaseModel):
    ApiId: StrictStr
    Name: StrictStr
    Schema: StrictStr
    ContentType: StrictStr | None = None
    Description: StrictStr | None = None
