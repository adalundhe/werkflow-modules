from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchNetworkInterface(BaseModel):
    attachmentId: StrictStr | None = None
    ipv6Address: StrictStr | None = None
    privateIpv4Address: StrictStr | None = None
