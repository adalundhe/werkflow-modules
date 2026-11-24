from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_validation_token_detail import CloudFrontValidationTokenDetail


class CloudFrontManagedCertificateDetails(BaseModel):
    CertificateArn: StrictStr | None = None
    CertificateStatus: StrictStr | None = None
    ValidationTokenHost: StrictStr | None = None
    ValidationTokenDetails: list[CloudFrontValidationTokenDetail] | None = None
