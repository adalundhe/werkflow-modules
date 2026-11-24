from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AmplifyGetArtifactUrlResponse(BaseModel):
    artifactId: StrictStr | None = None
    artifactUrl: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
