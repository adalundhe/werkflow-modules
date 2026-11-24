from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactUpstreamRepositoryModel(BaseModel):
    repositoryName: StrictStr
