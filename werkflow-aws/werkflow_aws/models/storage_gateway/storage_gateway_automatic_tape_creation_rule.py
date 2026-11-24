from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class StorageGatewayAutomaticTapeCreationRule(BaseModel):
    TapeBarcodePrefix: StrictStr | None = None
    PoolId: StrictStr | None = None
    TapeSizeInBytes: StrictInt | None = None
    MinimumNumTapes: StrictInt | None = None
    Worm: StrictBool | None = None
