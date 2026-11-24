from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2Section(BaseModel):
    ProductRestEndpointPageArns: list[StrictStr] | None = None
    SectionName: StrictStr | None = None
