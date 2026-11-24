from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_pipeline_deploy_action_execution_target import CodePipelineDeployActionExecutionTarget


class CodePipelineListDeployActionExecutionTargetsResponse(BaseModel):
    targets: list[CodePipelineDeployActionExecutionTarget] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
