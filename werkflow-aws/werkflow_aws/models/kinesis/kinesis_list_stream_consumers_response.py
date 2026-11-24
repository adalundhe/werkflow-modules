from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_consumer import KinesisConsumer


class KinesisListStreamConsumersResponse(BaseModel):
    Consumers: list[KinesisConsumer] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
