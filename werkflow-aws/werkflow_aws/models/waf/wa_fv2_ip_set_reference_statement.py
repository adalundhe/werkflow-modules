from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_ip_set_forwarded_ip_config import WAFv2IPSetForwardedIPConfig


class WAFv2IPSetReferenceStatement(BaseModel):
    ARN: StrictStr | None = None
    IPSetForwardedIPConfig: WAFv2IPSetForwardedIPConfig | None = None
