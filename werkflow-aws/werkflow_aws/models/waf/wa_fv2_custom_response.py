from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_custom_http_header import WAFv2CustomHTTPHeader


class WAFv2CustomResponse(BaseModel):
    ResponseCode: StrictInt | None = None
    CustomResponseBodyKey: StrictStr | None = None
    ResponseHeaders: list[WAFv2CustomHTTPHeader] | None = None
