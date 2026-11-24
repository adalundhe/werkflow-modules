from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceHybridSettingsDescription(BaseModel):
    SelfManagedDnsIpAddrs: list[StrictStr] | None = None
    SelfManagedInstanceIds: list[StrictStr] | None = None
