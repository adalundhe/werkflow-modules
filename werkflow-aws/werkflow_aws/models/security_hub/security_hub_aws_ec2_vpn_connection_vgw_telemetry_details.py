from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEc2VpnConnectionVgwTelemetryDetails(BaseModel):
    AcceptedRouteCount: StrictInt | None = None
    CertificateArn: StrictStr | None = None
    LastStatusChange: StrictStr | None = None
    OutsideIpAddress: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
