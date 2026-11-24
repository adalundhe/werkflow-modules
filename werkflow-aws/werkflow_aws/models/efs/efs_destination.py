from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EFSDestination(BaseModel):
    Status: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    Region: StrictStr | None = None
    LastReplicatedTimestamp: datetime.datetime | StrictStr | None = None
    OwnerId: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    RoleArn: StrictStr | None = None
