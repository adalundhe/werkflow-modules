from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class CodePipelinePutActionRevisionResponse(BaseModel):
    newRevision: StrictBool | None = None
    pipelineExecutionId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
