from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2AccessLogSettings(BaseModel):
    DestinationArn: StrictStr | None = None
    Format: StrictStr | None = None
