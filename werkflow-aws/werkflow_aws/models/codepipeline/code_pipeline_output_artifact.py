from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodePipelineOutputArtifact(BaseModel):
    name: StrictStr | None = None
    files: list[StrictStr] | None = None
