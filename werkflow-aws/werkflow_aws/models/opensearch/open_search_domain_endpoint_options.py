from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchDomainEndpointOptions(BaseModel):
    EnforceHTTPS: StrictBool | None = None
    TLSSecurityPolicy: StrictStr | None = None
    CustomEndpointEnabled: StrictBool | None = None
    CustomEndpoint: StrictStr | None = None
    CustomEndpointCertificateArn: StrictStr | None = None
