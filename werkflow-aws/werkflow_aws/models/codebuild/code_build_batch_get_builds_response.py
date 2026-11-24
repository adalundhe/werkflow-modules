from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_build_build import CodeBuildBuild


class CodeBuildBatchGetBuildsResponse(BaseModel):
    builds: list[CodeBuildBuild] | None = None
    buildsNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
