from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_build_project import CodeBuildProject


class CodeBuildBatchGetProjectsResponse(BaseModel):
    projects: list[CodeBuildProject] | None = None
    projectsNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
