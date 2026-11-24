from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_front_ca_certificates_bundle_source import CloudFrontCaCertificatesBundleSource


class CloudFrontUpdateTrustStoreRequest(BaseModel):
    Id: StrictStr
    IfMatch: StrictStr
    CaCertificatesBundleSource: CloudFrontCaCertificatesBundleSource | None = None
    UseClientCertificateOCSPEndpoint: StrictBool | None = None
