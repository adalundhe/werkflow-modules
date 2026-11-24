from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MemoryDBServiceUpdate(BaseModel):
    ClusterName: StrictStr | None = None
    ServiceUpdateName: StrictStr | None = None
    ReleaseDate: datetime.datetime | StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    Type: StrictStr | None = None
    Engine: StrictStr | None = None
    NodesUpdated: StrictStr | None = None
    AutoUpdateStartDate: datetime.datetime | StrictStr | None = None
