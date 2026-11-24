from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_build_sandbox import CodeBuildSandbox


class CodeBuildStopSandboxResponse(BaseModel):
    sandbox: CodeBuildSandbox | None = None
    ResponseMetadata: dict[str, Any] | None = None
