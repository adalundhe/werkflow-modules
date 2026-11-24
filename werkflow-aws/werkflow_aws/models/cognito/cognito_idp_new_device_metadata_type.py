from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPNewDeviceMetadataType(BaseModel):
    DeviceKey: StrictStr | None = None
    DeviceGroupKey: StrictStr | None = None
