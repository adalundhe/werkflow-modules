from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_engine_version import DMSEngineVersion


class DMSDescribeEngineVersionsResponse(BaseModel):
    EngineVersions: list[DMSEngineVersion] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
