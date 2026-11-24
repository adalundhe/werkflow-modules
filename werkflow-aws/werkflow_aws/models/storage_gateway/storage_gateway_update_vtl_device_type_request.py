from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayUpdateVTLDeviceTypeRequest(BaseModel):
    VTLDeviceARN: StrictStr
    DeviceType: StrictStr
