from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSPortMapping(BaseModel):
    containerPort: StrictInt | None = None
    hostPort: StrictInt | None = None
    protocol: StrictStr | None = None
    name: StrictStr | None = None
    appProtocol: StrictStr | None = None
    containerPortRange: StrictStr | None = None
