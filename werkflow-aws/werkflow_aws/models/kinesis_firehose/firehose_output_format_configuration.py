from __future__ import annotations
from pydantic import BaseModel
from .firehose_serializer import FirehoseSerializer


class FirehoseOutputFormatConfiguration(BaseModel):
    Serializer: FirehoseSerializer | None = None
