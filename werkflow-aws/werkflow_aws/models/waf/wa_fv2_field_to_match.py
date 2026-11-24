from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_all_query_arguments import WAFv2AllQueryArguments
from .wa_fv2_body import WAFv2Body
from .wa_fv2_cookies import WAFv2Cookies
from .wa_fv2_header_order import WAFv2HeaderOrder
from .wa_fv2_headers import WAFv2Headers
from .wa_fv2_ja3_fingerprint import WAFv2JA3Fingerprint
from .wa_fv2_ja4_fingerprint import WAFv2JA4Fingerprint
from .wa_fv2_json_body import WAFv2JsonBody
from .wa_fv2_method import WAFv2Method
from .wa_fv2_query_string import WAFv2QueryString
from .wa_fv2_single_header import WAFv2SingleHeader
from .wa_fv2_single_query_argument import WAFv2SingleQueryArgument
from .wa_fv2_uri_fragment import WAFv2UriFragment
from .wa_fv2_uri_path import WAFv2UriPath


class WAFv2FieldToMatch(BaseModel):
    SingleHeader: WAFv2SingleHeader | None = None
    SingleQueryArgument: WAFv2SingleQueryArgument | None = None
    AllQueryArguments: WAFv2AllQueryArguments | None = None
    UriPath: WAFv2UriPath | None = None
    QueryString: WAFv2QueryString | None = None
    Body: WAFv2Body | None = None
    Method: WAFv2Method | None = None
    JsonBody: WAFv2JsonBody | None = None
    Headers: WAFv2Headers | None = None
    Cookies: WAFv2Cookies | None = None
    HeaderOrder: WAFv2HeaderOrder | None = None
    JA3Fingerprint: WAFv2JA3Fingerprint | None = None
    JA4Fingerprint: WAFv2JA4Fingerprint | None = None
    UriFragment: WAFv2UriFragment | None = None
