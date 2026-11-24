from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2DisableVpcClassicLinkDnsSupportRequest(BaseModel):
    VpcId: StrictStr | None = None
