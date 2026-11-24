from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_subscribe_to_shard_event_stream import KinesisSubscribeToShardEventStream


class KinesisSubscribeToShardResponse(BaseModel):
    EventStream: KinesisSubscribeToShardEventStream | None = None
    ResponseMetadata: dict[str, Any] | None = None
