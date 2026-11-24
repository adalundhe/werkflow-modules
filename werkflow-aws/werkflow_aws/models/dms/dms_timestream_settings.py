from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSTimestreamSettings(BaseModel):
    DatabaseName: StrictStr | None = None
    MemoryDuration: StrictInt | None = None
    MagneticDuration: StrictInt | None = None
    CdcInsertsAndUpdates: StrictBool | None = None
    EnableMagneticStoreWrites: StrictBool | None = None
