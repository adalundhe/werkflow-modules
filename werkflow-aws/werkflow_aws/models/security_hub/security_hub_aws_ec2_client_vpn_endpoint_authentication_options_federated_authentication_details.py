from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails(BaseModel):
    SamlProviderArn: StrictStr | None = None
    SelfServiceSamlProviderArn: StrictStr | None = None
