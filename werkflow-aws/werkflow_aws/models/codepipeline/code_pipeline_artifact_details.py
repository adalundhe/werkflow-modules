from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CodePipelineArtifactDetails(BaseModel):
    minimumCount: StrictInt | None = None
    maximumCount: StrictInt | None = None
