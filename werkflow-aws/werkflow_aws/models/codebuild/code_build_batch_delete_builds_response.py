from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_build_build_not_deleted import CodeBuildBuildNotDeleted


class CodeBuildBatchDeleteBuildsResponse(BaseModel):
    buildsDeleted: list[StrictStr] | None = None
    buildsNotDeleted: list[CodeBuildBuildNotDeleted] | None = None
    ResponseMetadata: dict[str, Any] | None = None
