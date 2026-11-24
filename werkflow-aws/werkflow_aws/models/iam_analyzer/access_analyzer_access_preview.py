from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .access_analyzer_access_preview_status_reason import AccessAnalyzerAccessPreviewStatusReason
from .access_analyzer_configuration import AccessAnalyzerConfiguration


class AccessAnalyzerAccessPreview(BaseModel):
    id: StrictStr | None = None
    analyzerArn: StrictStr | None = None
    configurations: dict[StrictStr, AccessAnalyzerConfiguration] | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    statusReason: AccessAnalyzerAccessPreviewStatusReason | None = None
