from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_pipeline_action_type import CodePipelineActionType
from .code_pipeline_tag import CodePipelineTag


class CodePipelineCreateCustomActionTypeResponse(BaseModel):
    actionType: CodePipelineActionType | None = None
    tags: list[CodePipelineTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
