from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2EndpointConfigurationResponse(BaseModel):
    CertificateArn: StrictStr | None = None
    DomainName: StrictStr | None = None
    PortalDefaultDomainName: StrictStr | None = None
    PortalDomainHostedZoneId: StrictStr | None = None
