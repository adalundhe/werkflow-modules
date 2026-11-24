from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2IpamDiscoveryFailureReason(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
