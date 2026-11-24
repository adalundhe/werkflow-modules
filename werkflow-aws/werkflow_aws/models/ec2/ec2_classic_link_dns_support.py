from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2ClassicLinkDnsSupport(BaseModel):
    ClassicLinkDnsSupported: StrictBool | None = None
    VpcId: StrictStr | None = None
