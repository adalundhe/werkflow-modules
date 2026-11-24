from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_shard_filter import KinesisShardFilter


class KinesisListShardsRequest(BaseModel):
    StreamName: StrictStr | None = None
    NextToken: StrictStr | None = None
    ExclusiveStartShardId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    StreamCreationTimestamp: datetime.datetime | StrictStr | None = None
    ShardFilter: KinesisShardFilter | None = None
    StreamARN: StrictStr | None = None
    StreamId: StrictStr | None = None
