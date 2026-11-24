from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class SecurityHubAwsCloudFrontDistributionViewerCertificate(BaseModel):
    AcmCertificateArn: StrictStr | None = None
    Certificate: StrictStr | None = None
    CertificateSource: StrictStr | None = None
    CloudFrontDefaultCertificate: StrictBool | None = None
    IamCertificateId: StrictStr | None = None
    MinimumProtocolVersion: StrictStr | None = None
    SslSupportMethod: StrictStr | None = None
