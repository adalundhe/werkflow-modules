from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_http_header import WAFv2HTTPHeader


class WAFv2HTTPRequest(BaseModel):
    ClientIP: StrictStr | None = None
    Country: StrictStr | None = None
    URI: StrictStr | None = None
    Method: StrictStr | None = None
    HTTPVersion: StrictStr | None = None
    Headers: list[WAFv2HTTPHeader] | None = None
