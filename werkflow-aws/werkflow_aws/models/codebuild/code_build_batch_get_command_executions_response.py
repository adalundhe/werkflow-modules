from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_build_command_execution import CodeBuildCommandExecution


class CodeBuildBatchGetCommandExecutionsResponse(BaseModel):
    commandExecutions: list[CodeBuildCommandExecution] | None = None
    commandExecutionsNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
