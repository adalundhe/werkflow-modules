from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class EC2DestinationOptionsRequest(BaseModel):
    FileFormat: Literal['plain-text', 'parquet'] | None = None
    HiveCompatiblePartitions: StrictBool | None = None
    PerHourPartition: StrictBool | None = None
