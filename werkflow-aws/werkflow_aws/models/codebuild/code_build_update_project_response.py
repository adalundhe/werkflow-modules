from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_build_project import CodeBuildProject


class CodeBuildUpdateProjectResponse(BaseModel):
    project: CodeBuildProject | None = None
    ResponseMetadata: dict[str, Any] | None = None
