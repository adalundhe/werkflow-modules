from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayCreateTapesRequest(BaseModel):
    GatewayARN: StrictStr
    TapeSizeInBytes: StrictInt
    ClientToken: StrictStr
    NumTapesToCreate: StrictInt
    TapeBarcodePrefix: StrictStr
    KMSEncrypted: StrictBool | None = None
    KMSKey: StrictStr | None = None
    PoolId: StrictStr | None = None
    Worm: StrictBool | None = None
    Tags: list[StorageGatewayTag] | None = None
