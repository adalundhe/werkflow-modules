from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .firehose_processor import FirehoseProcessor


class FirehoseProcessingConfiguration(BaseModel):
    Enabled: StrictBool | None = None
    Processors: list[FirehoseProcessor] | None = None
