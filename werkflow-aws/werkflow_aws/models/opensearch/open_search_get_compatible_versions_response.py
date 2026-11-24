from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_compatible_versions_map import OpenSearchCompatibleVersionsMap


class OpenSearchGetCompatibleVersionsResponse(BaseModel):
    CompatibleVersions: list[OpenSearchCompatibleVersionsMap] | None = None
    ResponseMetadata: dict[str, Any] | None = None
