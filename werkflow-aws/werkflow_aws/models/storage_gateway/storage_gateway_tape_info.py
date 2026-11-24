from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayTapeInfo(BaseModel):
    TapeARN: StrictStr | None = None
    TapeBarcode: StrictStr | None = None
    TapeSizeInBytes: StrictInt | None = None
    TapeStatus: StrictStr | None = None
    GatewayARN: StrictStr | None = None
    PoolId: StrictStr | None = None
    RetentionStartDate: datetime.datetime | StrictStr | None = None
    PoolEntryDate: datetime.datetime | StrictStr | None = None
