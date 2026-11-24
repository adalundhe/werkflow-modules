from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSNetworkBinding(BaseModel):
    bindIP: StrictStr | None = None
    containerPort: StrictInt | None = None
    hostPort: StrictInt | None = None
    protocol: StrictStr | None = None
    containerPortRange: StrictStr | None = None
    hostPortRange: StrictStr | None = None
