from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_build_ssm_session import CodeBuildSSMSession


class CodeBuildStartSandboxConnectionResponse(BaseModel):
    ssmSession: CodeBuildSSMSession | None = None
    ResponseMetadata: dict[str, Any] | None = None
