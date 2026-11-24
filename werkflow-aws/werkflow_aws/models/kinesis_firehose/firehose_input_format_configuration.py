from __future__ import annotations
from pydantic import BaseModel
from .firehose_deserializer import FirehoseDeserializer


class FirehoseInputFormatConfiguration(BaseModel):
    Deserializer: FirehoseDeserializer | None = None
