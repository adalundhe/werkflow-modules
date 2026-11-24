from __future__ import annotations
from pydantic import BaseModel
from .acm_certificate_metadata_1 import AcmCertificateMetadata as _AcmCertificateMetadataType


class ACMCertificateMetadata(BaseModel):
    AcmCertificateMetadata: _AcmCertificateMetadataType | None = None
