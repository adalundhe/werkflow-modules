from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .document_db_engine_defaults import DocumentDBEngineDefaults


class DocumentDBDescribeEngineDefaultClusterParametersResponse(BaseModel):
    EngineDefaults: DocumentDBEngineDefaults | None = None
    ResponseMetadata: dict[str, Any] | None = None
