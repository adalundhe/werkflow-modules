from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fis_resolved_target import FISResolvedTarget


class FISListExperimentResolvedTargetsResponse(BaseModel):
    resolvedTargets: list[FISResolvedTarget] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
