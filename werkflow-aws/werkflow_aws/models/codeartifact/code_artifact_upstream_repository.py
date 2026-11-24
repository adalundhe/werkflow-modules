from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactUpstreamRepository(BaseModel):
    repositoryName: StrictStr
