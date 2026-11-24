from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_action_type_declaration import CodePipelineActionTypeDeclaration


class CodePipelineUpdateActionTypeRequest(BaseModel):
    actionType: CodePipelineActionTypeDeclaration
