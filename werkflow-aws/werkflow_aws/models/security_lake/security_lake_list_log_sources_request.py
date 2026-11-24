from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_lake_log_source_resource import SecurityLakeLogSourceResource


class SecurityLakeListLogSourcesRequest(BaseModel):
    accounts: list[StrictStr] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    regions: list[StrictStr] | None = None
    sources: list[SecurityLakeLogSourceResource] | None = None
