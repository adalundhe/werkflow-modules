from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .cloud_front_ca_certificates_bundle_source import CloudFrontCaCertificatesBundleSource
from .cloud_front_tags import CloudFrontTags


class CloudFrontCreateTrustStoreRequest(BaseModel):
    Name: StrictStr
    CaCertificatesBundleSource: CloudFrontCaCertificatesBundleSource
    UseClientCertificateOCSPEndpoint: StrictBool | None = None
    Tags: CloudFrontTags | None = None
