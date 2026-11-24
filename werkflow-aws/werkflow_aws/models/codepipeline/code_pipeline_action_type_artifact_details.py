from __future__ import annotations
from pydantic import BaseModel, StrictInt


class CodePipelineActionTypeArtifactDetails(BaseModel):
    minimumCount: StrictInt | None = None
    maximumCount: StrictInt | None = None
