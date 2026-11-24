from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsApiGatewayAccessLogSettings(BaseModel):
    Format: StrictStr | None = None
    DestinationArn: StrictStr | None = None
