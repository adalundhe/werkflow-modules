from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsEc2ClientVpnEndpointConnectionLogOptionsDetails(BaseModel):
    Enabled: StrictBool | None = None
    CloudwatchLogGroup: StrictStr | None = None
    CloudwatchLogStream: StrictStr | None = None
