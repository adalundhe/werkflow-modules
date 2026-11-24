from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisVideoUpdateDataRetentionRequest(BaseModel):
    CurrentVersion: StrictStr
    Operation: Literal['INCREASE_DATA_RETENTION', 'DECREASE_DATA_RETENTION']
    DataRetentionChangeInHours: StrictInt
    StreamName: StrictStr | None = None
    StreamARN: StrictStr | None = None
