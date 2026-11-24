from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsMskClusterClusterInfoClientAuthenticationTlsDetails(BaseModel):
    CertificateAuthorityArnList: list[StrictStr] | None = None
    Enabled: StrictBool | None = None
