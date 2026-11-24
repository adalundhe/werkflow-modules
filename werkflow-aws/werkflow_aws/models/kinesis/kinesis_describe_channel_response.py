from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_channel_description import KinesisChannelDescription


class KinesisDescribeChannelResponse(BaseModel):
    ChannelDescription: KinesisChannelDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
