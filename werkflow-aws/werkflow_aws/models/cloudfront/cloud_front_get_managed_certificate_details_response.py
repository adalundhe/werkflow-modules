from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_front_managed_certificate_details import CloudFrontManagedCertificateDetails


class CloudFrontGetManagedCertificateDetailsResponse(BaseModel):
    ManagedCertificateDetails: CloudFrontManagedCertificateDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
