from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .storage_gateway_tag import StorageGatewayTag


class StorageGatewayCreateTapeWithBarcodeRequest(BaseModel):
    GatewayARN: StrictStr
    TapeSizeInBytes: StrictInt
    TapeBarcode: StrictStr
    KMSEncrypted: StrictBool | None = None
    KMSKey: StrictStr | None = None
    PoolId: StrictStr | None = None
    Worm: StrictBool | None = None
    Tags: list[StorageGatewayTag] | None = None
