from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2EnableVpcClassicLinkDnsSupportRequest(BaseModel):
    VpcId: StrictStr | None = None
