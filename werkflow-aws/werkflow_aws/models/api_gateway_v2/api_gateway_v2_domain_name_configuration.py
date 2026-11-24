from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class APIGatewayV2DomainNameConfiguration(BaseModel):
    ApiGatewayDomainName: StrictStr | None = None
    CertificateArn: StrictStr | None = None
    CertificateName: StrictStr | None = None
    CertificateUploadDate: datetime.datetime | StrictStr | None = None
    DomainNameStatus: StrictStr | None = None
    DomainNameStatusMessage: StrictStr | None = None
    EndpointType: StrictStr | None = None
    HostedZoneId: StrictStr | None = None
    IpAddressType: StrictStr | None = None
    SecurityPolicy: StrictStr | None = None
    OwnershipVerificationCertificateArn: StrictStr | None = None
