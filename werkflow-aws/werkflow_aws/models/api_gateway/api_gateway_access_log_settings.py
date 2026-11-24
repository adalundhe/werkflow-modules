from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayAccessLogSettings(BaseModel):
    format: StrictStr | None = None
    destinationArn: StrictStr | None = None
