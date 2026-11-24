from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .timestream_write_magnetic_store_rejected_data_location import TimestreamWriteMagneticStoreRejectedDataLocation


class TimestreamWriteMagneticStoreWriteProperties(BaseModel):
    EnableMagneticStoreWrites: StrictBool | None = None
    MagneticStoreRejectedDataLocation: TimestreamWriteMagneticStoreRejectedDataLocation | None = None
