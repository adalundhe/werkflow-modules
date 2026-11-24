from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_response_headers_policy_cors_config import CloudFrontResponseHeadersPolicyCorsConfig
from .cloud_front_response_headers_policy_custom_headers_config import CloudFrontResponseHeadersPolicyCustomHeadersConfig
from .cloud_front_response_headers_policy_remove_headers_config import CloudFrontResponseHeadersPolicyRemoveHeadersConfig
from .cloud_front_response_headers_policy_security_headers_config import CloudFrontResponseHeadersPolicySecurityHeadersConfig
from .cloud_front_response_headers_policy_server_timing_headers_config import CloudFrontResponseHeadersPolicyServerTimingHeadersConfig


class CloudFrontResponseHeadersPolicyConfig(BaseModel):
    Comment: StrictStr | None = None
    Name: StrictStr | None = None
    CorsConfig: CloudFrontResponseHeadersPolicyCorsConfig | None = None
    SecurityHeadersConfig: CloudFrontResponseHeadersPolicySecurityHeadersConfig | None = None
    ServerTimingHeadersConfig: CloudFrontResponseHeadersPolicyServerTimingHeadersConfig | None = None
    CustomHeadersConfig: CloudFrontResponseHeadersPolicyCustomHeadersConfig | None = None
    RemoveHeadersConfig: CloudFrontResponseHeadersPolicyRemoveHeadersConfig | None = None
