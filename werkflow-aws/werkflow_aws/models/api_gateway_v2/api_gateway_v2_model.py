from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2Model(BaseModel):
    ContentType: StrictStr | None = None
    Description: StrictStr | None = None
    ModelId: StrictStr | None = None
    Name: StrictStr | None = None
    Schema: StrictStr | None = None
