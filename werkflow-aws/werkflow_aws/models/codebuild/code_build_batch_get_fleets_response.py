from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_build_fleet import CodeBuildFleet


class CodeBuildBatchGetFleetsResponse(BaseModel):
    fleets: list[CodeBuildFleet] | None = None
    fleetsNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
