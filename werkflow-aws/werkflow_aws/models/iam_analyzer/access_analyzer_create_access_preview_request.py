from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_configuration import AccessAnalyzerConfiguration


class AccessAnalyzerCreateAccessPreviewRequest(BaseModel):
    analyzerArn: StrictStr
    configurations: dict[StrictStr, AccessAnalyzerConfiguration]
    clientToken: StrictStr | None = None
