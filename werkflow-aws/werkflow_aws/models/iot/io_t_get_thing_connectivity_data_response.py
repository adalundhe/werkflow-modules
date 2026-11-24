from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTGetThingConnectivityDataResponse(BaseModel):
    thingName: StrictStr | None = None
    connected: StrictBool | None = None
    timestamp: datetime.datetime | StrictStr | None = None
    disconnectReason: StrictStr | None = None
    sourceIp: StrictStr | None = None
    sourcePort: StrictInt | None = None
    targetIp: StrictStr | None = None
    targetPort: StrictInt | None = None
    vpcEndpointId: StrictStr | None = None
    keepAliveDuration: StrictInt | None = None
    cleanSession: StrictBool | None = None
    sessionExpiry: StrictInt | None = None
    clientId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
