from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kinesis_channel_stream_identifier import KinesisChannelStreamIdentifier


class KinesisChannelSummary(BaseModel):
    ChannelName: StrictStr | None = None
    ChannelARN: StrictStr | None = None
    ChannelId: StrictStr | None = None
    ChannelStatus: StrictStr | None = None
    ChannelStatusReason: StrictStr | None = None
    ChannelCreationTimestamp: datetime.datetime | StrictStr | None = None
    ChannelDestinationType: StrictStr | None = None
    Streams: list[KinesisChannelStreamIdentifier] | None = None
