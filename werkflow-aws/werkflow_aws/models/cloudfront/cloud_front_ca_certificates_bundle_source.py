from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_ca_certificates_bundle_s3_location import CloudFrontCaCertificatesBundleS3Location


class CloudFrontCaCertificatesBundleSource(BaseModel):
    CaCertificatesBundleS3Location: CloudFrontCaCertificatesBundleS3Location | None = None
