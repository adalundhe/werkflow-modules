from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_pipeline_action_type_declaration import CodePipelineActionTypeDeclaration


class CodePipelineGetActionTypeResponse(BaseModel):
    actionType: CodePipelineActionTypeDeclaration | None = None
    ResponseMetadata: dict[str, Any] | None = None
