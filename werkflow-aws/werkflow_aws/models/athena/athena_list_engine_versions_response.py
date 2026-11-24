from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .athena_engine_version_model import AthenaEngineVersionModel


class AthenaListEngineVersionsResponse(BaseModel):
    EngineVersions: list[AthenaEngineVersionModel] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
