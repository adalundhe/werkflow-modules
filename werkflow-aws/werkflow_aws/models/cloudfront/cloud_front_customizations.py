from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_certificate import CloudFrontCertificate
from .cloud_front_geo_restriction_customization import CloudFrontGeoRestrictionCustomization
from .cloud_front_web_acl_customization import CloudFrontWebAclCustomization


class CloudFrontCustomizations(BaseModel):
    WebAcl: CloudFrontWebAclCustomization | None = None
    Certificate: CloudFrontCertificate | None = None
    GeoRestrictions: CloudFrontGeoRestrictionCustomization | None = None
