from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyGetArtifactUrlRequest(BaseModel):
    artifactId: StrictStr
