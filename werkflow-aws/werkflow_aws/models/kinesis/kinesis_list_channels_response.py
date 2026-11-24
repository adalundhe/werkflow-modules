from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_channel_summary import KinesisChannelSummary


class KinesisListChannelsResponse(BaseModel):
    ChannelSummaries: list[KinesisChannelSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
