from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_stage_state import CodePipelineStageState


class CodePipelineGetPipelineStateResponse(BaseModel):
    pipelineName: StrictStr | None = None
    pipelineVersion: StrictInt | None = None
    stageStates: list[CodePipelineStageState] | None = None
    created: datetime.datetime | StrictStr | None = None
    updated: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
