from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceHybridUpdateValue(BaseModel):
    InstanceIds: list[StrictStr] | None = None
    DnsIps: list[StrictStr] | None = None
