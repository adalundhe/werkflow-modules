from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_build_command_execution import CodeBuildCommandExecution


class CodeBuildStartCommandExecutionResponse(BaseModel):
    commandExecution: CodeBuildCommandExecution | None = None
    ResponseMetadata: dict[str, Any] | None = None
