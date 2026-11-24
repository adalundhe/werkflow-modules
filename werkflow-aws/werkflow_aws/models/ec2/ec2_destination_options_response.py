from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DestinationOptionsResponse(BaseModel):
    FileFormat: StrictStr | None = None
    HiveCompatiblePartitions: StrictBool | None = None
    PerHourPartition: StrictBool | None = None
