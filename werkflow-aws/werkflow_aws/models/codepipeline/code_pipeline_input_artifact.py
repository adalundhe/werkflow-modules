from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineInputArtifact(BaseModel):
    name: StrictStr | None = None
