from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acm_certificate_metadata import ACMCertificateMetadata
from .acmx509_attributes import ACMX509Attributes


class ACMCertificateSearchResult(BaseModel):
    CertificateArn: StrictStr | None = None
    X509Attributes: ACMX509Attributes | None = None
    CertificateMetadata: ACMCertificateMetadata | None = None
