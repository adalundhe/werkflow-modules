from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_rate_limit_asn import WAFv2RateLimitAsn
from .wa_fv2_rate_limit_cookie import WAFv2RateLimitCookie
from .wa_fv2_rate_limit_forwarded_ip import WAFv2RateLimitForwardedIP
from .wa_fv2_rate_limit_http_method import WAFv2RateLimitHTTPMethod
from .wa_fv2_rate_limit_header import WAFv2RateLimitHeader
from .wa_fv2_rate_limit_ip import WAFv2RateLimitIP
from .wa_fv2_rate_limit_ja3_fingerprint import WAFv2RateLimitJA3Fingerprint
from .wa_fv2_rate_limit_ja4_fingerprint import WAFv2RateLimitJA4Fingerprint
from .wa_fv2_rate_limit_label_namespace import WAFv2RateLimitLabelNamespace
from .wa_fv2_rate_limit_query_argument import WAFv2RateLimitQueryArgument
from .wa_fv2_rate_limit_query_string import WAFv2RateLimitQueryString
from .wa_fv2_rate_limit_uri_path import WAFv2RateLimitUriPath


class WAFv2RateBasedStatementCustomKey(BaseModel):
    Header: WAFv2RateLimitHeader | None = None
    Cookie: WAFv2RateLimitCookie | None = None
    QueryArgument: WAFv2RateLimitQueryArgument | None = None
    QueryString: WAFv2RateLimitQueryString | None = None
    HTTPMethod: WAFv2RateLimitHTTPMethod | None = None
    ForwardedIP: WAFv2RateLimitForwardedIP | None = None
    IP: WAFv2RateLimitIP | None = None
    LabelNamespace: WAFv2RateLimitLabelNamespace | None = None
    UriPath: WAFv2RateLimitUriPath | None = None
    JA3Fingerprint: WAFv2RateLimitJA3Fingerprint | None = None
    JA4Fingerprint: WAFv2RateLimitJA4Fingerprint | None = None
    ASN: WAFv2RateLimitAsn | None = None
