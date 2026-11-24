from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .amplify_artifact import AmplifyArtifact


class AmplifyListArtifactsResponse(BaseModel):
    artifacts: list[AmplifyArtifact] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
