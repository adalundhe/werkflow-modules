from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_lake_data_lake_source import SecurityLakeDataLakeSource


class SecurityLakeGetDataLakeSourcesResponse(BaseModel):
    dataLakeArn: StrictStr | None = None
    dataLakeSources: list[SecurityLakeDataLakeSource] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
