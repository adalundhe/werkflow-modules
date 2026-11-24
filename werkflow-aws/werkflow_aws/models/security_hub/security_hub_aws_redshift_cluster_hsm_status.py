from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsRedshiftClusterHsmStatus(BaseModel):
    HsmClientCertificateIdentifier: StrictStr | None = None
    HsmConfigurationIdentifier: StrictStr | None = None
    Status: StrictStr | None = None
