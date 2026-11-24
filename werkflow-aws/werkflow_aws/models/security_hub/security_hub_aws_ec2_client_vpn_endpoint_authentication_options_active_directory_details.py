from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails(BaseModel):
    DirectoryId: StrictStr | None = None
