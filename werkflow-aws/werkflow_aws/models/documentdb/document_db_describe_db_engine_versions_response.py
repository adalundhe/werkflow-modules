from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .document_dbdb_engine_version import DocumentDBDBEngineVersion


class DocumentDBDescribeDBEngineVersionsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBEngineVersions: list[DocumentDBDBEngineVersion] | None = None
    ResponseMetadata: dict[str, Any] | None = None
