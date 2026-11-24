from __future__ import annotations
from pydantic import BaseModel
from .access_analyzer_internal_access_configuration import AccessAnalyzerInternalAccessConfiguration
from .access_analyzer_unused_access_configuration import AccessAnalyzerUnusedAccessConfiguration


class AccessAnalyzerAnalyzerConfiguration(BaseModel):
    unusedAccess: AccessAnalyzerUnusedAccessConfiguration | None = None
    internalAccess: AccessAnalyzerInternalAccessConfiguration | None = None
