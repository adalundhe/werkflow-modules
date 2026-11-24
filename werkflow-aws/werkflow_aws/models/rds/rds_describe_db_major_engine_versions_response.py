from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_major_engine_version import RDSDBMajorEngineVersion


class RDSDescribeDBMajorEngineVersionsResponse(BaseModel):
    DBMajorEngineVersions: list[RDSDBMajorEngineVersion] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
