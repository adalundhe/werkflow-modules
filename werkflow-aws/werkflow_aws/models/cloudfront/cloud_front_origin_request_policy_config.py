from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_front_origin_request_policy_cookies_config import CloudFrontOriginRequestPolicyCookiesConfig
from .cloud_front_origin_request_policy_headers_config import CloudFrontOriginRequestPolicyHeadersConfig
from .cloud_front_origin_request_policy_query_strings_config import CloudFrontOriginRequestPolicyQueryStringsConfig


class CloudFrontOriginRequestPolicyConfig(BaseModel):
    Comment: StrictStr | None = None
    Name: StrictStr | None = None
    HeadersConfig: CloudFrontOriginRequestPolicyHeadersConfig | None = None
    CookiesConfig: CloudFrontOriginRequestPolicyCookiesConfig | None = None
    QueryStringsConfig: CloudFrontOriginRequestPolicyQueryStringsConfig | None = None
