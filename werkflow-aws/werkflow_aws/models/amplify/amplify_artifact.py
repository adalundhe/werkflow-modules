from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyArtifact(BaseModel):
    artifactFileName: StrictStr | None = None
    artifactId: StrictStr | None = None
