from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTThingConnectivity(BaseModel):
    connected: StrictBool | None = None
    timestamp: StrictInt | None = None
    disconnectReason: StrictStr | None = None
    keepAliveDuration: StrictInt | None = None
    cleanSession: StrictBool | None = None
    sessionExpiry: StrictInt | None = None
    clientId: StrictStr | None = None
