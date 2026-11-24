from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .wa_fv2_forwarded_ip_config import WAFv2ForwardedIPConfig


class WAFv2AsnMatchStatement(BaseModel):
    AsnList: list[StrictInt] | None = None
    ForwardedIPConfig: WAFv2ForwardedIPConfig | None = None
