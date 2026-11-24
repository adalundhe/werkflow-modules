from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_resource_profile_artifact import MacieResourceProfileArtifact


class MacieListResourceProfileArtifactsResponse(BaseModel):
    artifacts: list[MacieResourceProfileArtifact] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
