from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_analyzer_configuration import AccessAnalyzerAnalyzerConfiguration


class AccessAnalyzerUpdateAnalyzerRequest(BaseModel):
    analyzerName: StrictStr
    configuration: AccessAnalyzerAnalyzerConfiguration | None = None
