from __future__ import annotations
from pydantic import BaseModel
from .wa_fv2_custom_request_handling import WAFv2CustomRequestHandling


class WAFv2AllowAction(BaseModel):
    CustomRequestHandling: WAFv2CustomRequestHandling | None = None
