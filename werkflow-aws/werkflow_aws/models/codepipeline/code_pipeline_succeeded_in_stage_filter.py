from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineSucceededInStageFilter(BaseModel):
    stageName: StrictStr | None = None
