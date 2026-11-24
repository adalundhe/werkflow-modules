from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsOpenSearchServiceDomainDomainEndpointOptionsDetails(BaseModel):
    CustomEndpointCertificateArn: StrictStr | None = None
    CustomEndpointEnabled: StrictBool | None = None
    EnforceHTTPS: StrictBool | None = None
    CustomEndpoint: StrictStr | None = None
    TLSSecurityPolicy: StrictStr | None = None
