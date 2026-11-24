from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_custom_http_header import WAFv2CustomHTTPHeader


class WAFv2CustomRequestHandling(BaseModel):
    InsertHeaders: list[WAFv2CustomHTTPHeader] | None = None
