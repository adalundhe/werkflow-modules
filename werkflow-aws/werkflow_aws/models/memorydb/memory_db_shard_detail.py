from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .memory_db_shard_configuration import MemoryDBShardConfiguration


class MemoryDBShardDetail(BaseModel):
    Name: StrictStr | None = None
    Configuration: MemoryDBShardConfiguration | None = None
    Size: StrictStr | None = None
    SnapshotCreationTime: datetime.datetime | StrictStr | None = None
