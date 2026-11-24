from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_warm_throughput_object import KinesisWarmThroughputObject


class KinesisUpdateStreamWarmThroughputResponse(BaseModel):
    StreamARN: StrictStr | None = None
    StreamName: StrictStr | None = None
    WarmThroughput: KinesisWarmThroughputObject | None = None
    ResponseMetadata: dict[str, Any] | None = None
