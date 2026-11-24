from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2UpdateModelRequest(BaseModel):
    ApiId: StrictStr
    ModelId: StrictStr
    ContentType: StrictStr | None = None
    Description: StrictStr | None = None
    Name: StrictStr | None = None
    Schema: StrictStr | None = None
