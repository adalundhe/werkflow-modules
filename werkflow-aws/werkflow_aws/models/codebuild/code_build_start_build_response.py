from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_build_build import CodeBuildBuild


class CodeBuildStartBuildResponse(BaseModel):
    build: CodeBuildBuild | None = None
    ResponseMetadata: dict[str, Any] | None = None
