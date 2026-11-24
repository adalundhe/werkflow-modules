from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .support_severity_level import SupportSeverityLevel


class SupportDescribeSeverityLevelsResponse(BaseModel):
    severityLevels: list[SupportSeverityLevel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
