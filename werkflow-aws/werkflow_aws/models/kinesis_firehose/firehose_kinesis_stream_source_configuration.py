from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FirehoseKinesisStreamSourceConfiguration(BaseModel):
    KinesisStreamARN: StrictStr
    RoleARN: StrictStr
