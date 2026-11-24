from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmRemoteAccessEndpoints(BaseModel):
    remoteDriverEndpoint: StrictStr | None = None
    interactiveEndpoint: StrictStr | None = None
