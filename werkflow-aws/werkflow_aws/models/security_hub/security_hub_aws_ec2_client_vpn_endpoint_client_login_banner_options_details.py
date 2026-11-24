from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails(BaseModel):
    Enabled: StrictBool | None = None
    BannerText: StrictStr | None = None
