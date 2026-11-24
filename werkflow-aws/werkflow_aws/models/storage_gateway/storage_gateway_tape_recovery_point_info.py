from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayTapeRecoveryPointInfo(BaseModel):
    TapeARN: StrictStr | None = None
    TapeRecoveryPointTime: datetime.datetime | StrictStr | None = None
    TapeSizeInBytes: StrictInt | None = None
    TapeStatus: StrictStr | None = None
