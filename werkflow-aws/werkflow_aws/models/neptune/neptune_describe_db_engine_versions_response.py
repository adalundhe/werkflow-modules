from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_db_engine_version import NeptuneDBEngineVersion


class NeptuneDescribeDBEngineVersionsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBEngineVersions: list[NeptuneDBEngineVersion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
