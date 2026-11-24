from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_consumer_description import KinesisConsumerDescription


class KinesisDescribeStreamConsumerResponse(BaseModel):
    ConsumerDescription: KinesisConsumerDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
