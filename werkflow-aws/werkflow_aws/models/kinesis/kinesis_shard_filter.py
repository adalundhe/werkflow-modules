from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class KinesisShardFilter(BaseModel):
    Type: Literal['AFTER_SHARD_ID', 'AT_TRIM_HORIZON', 'FROM_TRIM_HORIZON', 'AT_LATEST', 'AT_TIMESTAMP', 'FROM_TIMESTAMP']
    ShardId: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
