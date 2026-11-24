from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MSKConsumerGroupReplication(BaseModel):
    ConsumerGroupsToExclude: list[StrictStr] | None = None
    ConsumerGroupsToReplicate: list[StrictStr] | None = None
    DetectAndCopyNewConsumerGroups: StrictBool | None = None
    SynchroniseConsumerGroupOffsets: StrictBool | None = None
    ConsumerGroupOffsetSyncMode: StrictStr | None = None
