from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFrontViewerCertificate(BaseModel):
    CloudFrontDefaultCertificate: StrictBool | None = None
    IAMCertificateId: StrictStr | None = None
    ACMCertificateArn: StrictStr | None = None
    SSLSupportMethod: StrictStr | None = None
    MinimumProtocolVersion: StrictStr | None = None
    Certificate: StrictStr | None = None
    CertificateSource: StrictStr | None = None
