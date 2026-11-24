from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_pipeline_action_type import CodePipelineActionType


class CodePipelineListActionTypesResponse(BaseModel):
    actionTypes: list[CodePipelineActionType] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
