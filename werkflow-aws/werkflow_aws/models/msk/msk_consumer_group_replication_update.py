from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MSKConsumerGroupReplicationUpdate(BaseModel):
    ConsumerGroupsToExclude: list[StrictStr]
    ConsumerGroupsToReplicate: list[StrictStr]
    DetectAndCopyNewConsumerGroups: StrictBool
    SynchroniseConsumerGroupOffsets: StrictBool
