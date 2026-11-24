from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .access_analyzer_analyzer_configuration import AccessAnalyzerAnalyzerConfiguration


class AccessAnalyzerUpdateAnalyzerResponse(BaseModel):
    configuration: AccessAnalyzerAnalyzerConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
