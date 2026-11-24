from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_engine_version import RDSDBEngineVersion


class RDSDescribeDBEngineVersionsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBEngineVersions: list[RDSDBEngineVersion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
