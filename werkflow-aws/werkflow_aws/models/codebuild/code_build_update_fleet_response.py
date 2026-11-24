from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_build_fleet import CodeBuildFleet


class CodeBuildUpdateFleetResponse(BaseModel):
    fleet: CodeBuildFleet | None = None
    ResponseMetadata: dict[str, Any] | None = None
