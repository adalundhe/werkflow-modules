from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_consumer import KinesisConsumer


class KinesisRegisterStreamConsumerResponse(BaseModel):
    Consumer: KinesisConsumer | None = None
    ResponseMetadata: dict[str, Any] | None = None
