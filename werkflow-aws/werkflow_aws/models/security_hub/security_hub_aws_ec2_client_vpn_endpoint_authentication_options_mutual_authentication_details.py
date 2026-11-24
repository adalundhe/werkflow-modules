from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails(BaseModel):
    ClientRootCertificateChain: StrictStr | None = None
