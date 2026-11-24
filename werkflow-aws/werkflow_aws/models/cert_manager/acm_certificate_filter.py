from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .acmx509_attribute_filter import ACMX509AttributeFilter
from .acm_certificate_metadata_filter import AcmCertificateMetadataFilter as _AcmCertificateMetadataFilterType


class ACMCertificateFilter(BaseModel):
    CertificateArn: StrictStr | None = None
    X509AttributeFilter: ACMX509AttributeFilter | None = None
    AcmCertificateMetadataFilter: _AcmCertificateMetadataFilterType | None = None
