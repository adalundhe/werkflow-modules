from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_log_source_resource import SecurityLakeLogSourceResource


class SecurityLakeLogSource(BaseModel):
    account: StrictStr | None = None
    region: StrictStr | None = None
    sources: list[SecurityLakeLogSourceResource] | None = None
