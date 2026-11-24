from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildResolvedArtifact(BaseModel):
    type: StrictStr | None = None
    location: StrictStr | None = None
    identifier: StrictStr | None = None
