from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .cloud_front_response_headers_policy_access_control_allow_headers import CloudFrontResponseHeadersPolicyAccessControlAllowHeaders
from .cloud_front_response_headers_policy_access_control_allow_methods import CloudFrontResponseHeadersPolicyAccessControlAllowMethods
from .cloud_front_response_headers_policy_access_control_allow_origins import CloudFrontResponseHeadersPolicyAccessControlAllowOrigins
from .cloud_front_response_headers_policy_access_control_expose_headers import CloudFrontResponseHeadersPolicyAccessControlExposeHeaders


class CloudFrontResponseHeadersPolicyCorsConfig(BaseModel):
    AccessControlAllowOrigins: CloudFrontResponseHeadersPolicyAccessControlAllowOrigins | None = None
    AccessControlAllowHeaders: CloudFrontResponseHeadersPolicyAccessControlAllowHeaders | None = None
    AccessControlAllowMethods: CloudFrontResponseHeadersPolicyAccessControlAllowMethods | None = None
    AccessControlAllowCredentials: StrictBool | None = None
    AccessControlExposeHeaders: CloudFrontResponseHeadersPolicyAccessControlExposeHeaders | None = None
    AccessControlMaxAgeSec: StrictInt | None = None
    OriginOverride: StrictBool | None = None
