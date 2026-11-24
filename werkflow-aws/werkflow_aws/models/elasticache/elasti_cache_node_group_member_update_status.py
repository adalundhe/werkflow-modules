from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ElastiCacheNodeGroupMemberUpdateStatus(BaseModel):
    CacheClusterId: StrictStr | None = None
    CacheNodeId: StrictStr | None = None
    NodeUpdateStatus: StrictStr | None = None
    NodeDeletionDate: datetime.datetime | StrictStr | None = None
    NodeUpdateStartDate: datetime.datetime | StrictStr | None = None
    NodeUpdateEndDate: datetime.datetime | StrictStr | None = None
    NodeUpdateInitiatedBy: StrictStr | None = None
    NodeUpdateInitiatedDate: datetime.datetime | StrictStr | None = None
    NodeUpdateStatusModifiedDate: datetime.datetime | StrictStr | None = None
