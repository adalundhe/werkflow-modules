from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .memory_db_endpoint import MemoryDBEndpoint


class MemoryDBNode(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    Endpoint: MemoryDBEndpoint | None = None
