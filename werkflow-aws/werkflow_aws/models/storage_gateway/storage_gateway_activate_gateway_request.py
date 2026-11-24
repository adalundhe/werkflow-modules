from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayActivateGatewayRequest(BaseModel):
    ActivationKey: StrictStr
    GatewayName: StrictStr
    GatewayTimezone: StrictStr
    GatewayRegion: StrictStr
    GatewayType: StrictStr | None = None
    TapeDriveType: StrictStr | None = None
    MediumChangerType: StrictStr | None = None
    Tags: list[StorageGatewayTag] | None = None
